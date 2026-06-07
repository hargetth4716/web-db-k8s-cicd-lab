# 네트워크 설계

## 네트워크 대역

| 항목 | 값 |
|---|---|
| 서브넷 | 192.168.150.0/24 |
| 게이트웨이 | 192.168.150.1 |
| 넷마스크 | 255.255.255.0 |

---

## VM IP 구성표

| VM 이름 | IP 주소 | 역할 |
|---|---|---|
| k8s-control-01 | 192.168.150.10 | Kubernetes Control Plane |
| k8s-worker-01 | 192.168.150.11 | Application Worker |
| k8s-worker-02 | 192.168.150.12 | DB / Monitoring Worker |
| cicd-runner-01 | 192.168.150.20 | CI/CD Runner |
| ops-tools-01 | 192.168.150.30 | 운영 관리 서버 |

---

## 서비스 접근 흐름

외부 클라이언트
  ↓
Ingress Controller (192.168.150.11 or 192.168.150.12 NodePort)
  ↓
Frontend Service
  ↓
Backend API Service
  ↓
PostgreSQL Service (ClusterIP)