# DCSM Week 4 — Java RMI & gRPC (Java + Python) Labs

> Repository ini berisi proyek praktikum Distributed Computing & Security Model (Week 4)  
> Implementasi:  
> - **Java RMI** (Remote Method Invocation)  
> - **gRPC** lintas bahasa: Java & Python

---

## 📁 Struktur Proyek

```

dcsm-week4/
├── grpc-lab/
│   ├── java/          ← implementasi gRPC di Java
│   └── python/        ← implementasi gRPC di Python
└── rmi-lab/           ← implementasi Java RMI

```

Setiap subfolder (java, python, rmi) punya:
- `Dockerfile`, `docker-compose.yml`
- Kode sumber (Java / Python)
- File `.dockerignore` & `.gitignore`

Selain itu, di root terdapat:
- `docker-compose.yml` global (kombinasi semua lab)
- Skrip bantu (misal `thelol.sh`) untuk menjalankan lab-lab secara mudah
- `.gitattributes`, `.dockerignore` global, `.gitignore` global

---

## 🚀 Cara Menjalankan

### Dengan skrip bantu (disarankan)

```bash
chmod +x thelol.sh
./thelol.sh
```

Jalankan semua

```bash
./thelol.sh up all
```

Atau jalankan subset:

```bash
./thelol.sh up rmi grpc-java
./thelol.sh up grpc-python
```

Stop semua:

```bash
./thelol.sh down
```

Cek status:

```bash
./thelol.sh status
```

---

### Tanpa skrip: menggunakan Docker Compose langsung

Di root:

```bash
docker-compose --profile rmi --profile grpc-java --profile grpc-python up -d --build
```

Atau untuk hanya satu lab:

```bash
docker-compose --profile rmi up -d --build
docker-compose --profile grpc-java up -d --build
docker-compose --profile grpc-python up -d --build
```

---

## 🧪 Apa yang Dilakukan Setiap Lab

### Java RMI (`rmi-lab/`)

* `Hello.java` → interface remote
* `Server.java` → implementasi & bind ke registry port 1099
* `Client.java` → lookup dan invoke
* Jalankan menggunakan Docker container terpisah

### gRPC Java (`grpc-lab/java`)

* `hello.proto` → definisi service RPC
* `HelloServer.java` → implementasi gRPC server
* `HelloClient.java` → client yang memanggil server
* Dibuild sebagai fat jar menggunakan Gradle + plugin Shadow

### gRPC Python (`grpc-lab/python`)

* `calculator.proto` (atau `hello.proto` versi Python)
* `server.py` → server Python gRPC
* `client.py` → client Python memanggil server
* Docker image memastikan output print langsung muncul (unbuffered)

---

## ✅ Capaian & Validasi

* Java RMI client/server berhasil saling berkomunikasi (Client menerima response dari Server)
* gRPC Java client/server menghasilkan output `Response: Hello, …`
* gRPC Python client/server menghasilkan `Add: …`, `Multiply: …`
* Semua dijalankan lewat Docker Compose & skrip bantu tanpa konflik port atau DNS resolver error

---

## 🧾 Lisensi & Penggunaan

MIT © Kevin Kresna, 2025. [MIT License](LICENSE)