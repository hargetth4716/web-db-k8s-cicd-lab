# Proxmox VM 설계

## 개요

Proxmox VE 위에 아래 VM을 구성한다. 처음은 5대로 시작하고, DB 분리 실습이 필요하면 db-01을 추가한다.

---

## VM 구성표

| VM 이름 | 역할 | vCPU | RAM | Disk | OS |
|---|---|---|---|---|---|
| k8s-control-01 | Kubernetes Control Plane | 2 | 4GB | 40GB | Ubuntu 22.04 |
| k8s-worker-01 | Application Worker | 4 | 8GB | 60GB | Ubuntu 22.04 |
| k8s-worker-02 | DB / Monitoring Worker | 4 | 8GB | 100GB | Ubuntu 22.04 |
| cicd-runner-01 | CI/CD Runner | 2 | 4GB | 60GB | Ubuntu 22.04 |
| ops-tools-01 | 운영 관리 서버 | 2 | 4GB | 40GB | Ubuntu 22.04 |

---

## 각 VM 역할 상세

**k8s-control-01**
- Kubernetes API Server, Scheduler, Controller Manager, etcd 실행
- kubeadm으로 클러스터 초기화
- kubectl 접근의 기준점

**k8s-worker-01**
- Frontend, Backend API Pod 실행
- 일반 애플리케이션 워크로드 담당

**k8s-worker-02**
- PostgreSQL StatefulSet 실행
- Prometheus, Grafana Pod 실행
- 디스크 용량이 큰 이유: DB 데이터 + 메트릭 저장

**cicd-runner-01**
- GitHub Actions Self-hosted Runner 설치
- Docker 빌드, kubectl 명령 실행
- GitHub과 직접 연결되는 유일한 내부 서버

**ops-tools-01**
- kubectl, helm, ansible, terraform, argocd CLI 설치
- 클러스터에 명령을 날리는 관리 접점
- 실제 운영 환경의 bastion host / jump server 역할과 유사

---

## Proxmox 설치 시 공통 설정

모든 VM에 공통 적용할 항목

- OS: Ubuntu 22.04 LTS (server)
- SSH 키 기반 인증 설정
- 기본 패키지: curl, wget, git, vim, net-tools
- 타임존: Asia/Seoul
- 스왑: Kubernetes 사용 시 k8s-control, worker에는 swap off 필요