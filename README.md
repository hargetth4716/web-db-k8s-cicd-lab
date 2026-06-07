# web-db-k8s-cicd-lab

> Proxmox 위에 Kubernetes 클러스터, CI/CD, 모니터링을 구성한 DevOps 포트폴리오 실습 프로젝트

---

## 프로젝트 목적

단순한 앱 개발이 아니라, 서비스를 실제 운영 환경과 유사하게 구성하고 배포·장애 대응·자동화·모니터링까지 경험하는 것을 목표로 한다.

---

## 전체 아키텍처

```text
Developer PC
  ↓ git push

GitHub Repository
  ↓ GitHub Actions (CI)

Container Registry
  ↓ image pull

Kubernetes Cluster (on Proxmox)
  ├─ Frontend Pod
  ├─ Backend API Pod
  ├─ PostgreSQL StatefulSet
  ├─ Ingress Controller
  ├─ ConfigMap / Secret
  └─ PVC

Monitoring
  ├─ Prometheus
  └─ Grafana