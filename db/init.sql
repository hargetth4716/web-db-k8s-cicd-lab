-- 데이터베이스 사용자 및 권한 설정
CREATE USER webuser WITH PASSWORD 'yourpassword';
GRANT ALL PRIVILEGES ON DATABASE webdb TO webuser;

-- posts 테이블 생성
CREATE TABLE IF NOT EXISTS posts (
    id          SERIAL PRIMARY KEY,
    title       VARCHAR(200) NOT NULL,
    content     TEXT NOT NULL,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 샘플 데이터 삽입
INSERT INTO posts (title, content) VALUES
    ('첫 번째 게시글', '이것은 DevOps 포트폴리오 실습용 첫 번째 게시글입니다.'),
    ('Kubernetes 학습', 'kubeadm으로 클러스터를 구성하고 flannel CNI를 설치했습니다.'),
    ('CI/CD 구성 중', 'GitHub Actions Self-hosted Runner를 설치하고 연동했습니다.');

-- webuser에게 테이블 권한 부여
GRANT ALL PRIVILEGES ON TABLE posts TO webuser;
GRANT USAGE, SELECT ON SEQUENCE posts_id_seq TO webuser;