# &lt;DB/&gt; Developments Berlad

---

## 🇪🇸 Español

¡Bienvenido a mi portafolio personal creado con Django! Este proyecto tiene como objetivo mostrar mis habilidades como desarrollador web y los proyectos en los que he trabajado.

### 🚀 Características

* Aplicación Django 100% funcional.
* Diseño moderno con interfaz responsiva y estética neon/cyberpunk.
* Sección de proyectos con imágenes y descripciones.
* **Gestión avanzada de certificados** con filtros dinámicos y acceso seguro a documentos PDF.
* Código limpio, modular y bien organizado.
* Variables de entorno gestionadas con `.env`.

### 🛠️ Tecnologías usadas

* Python & Django
* HTML5, CSS3, Bootstrap (con personalización neon)
* JavaScript (básico)
* SQLite / PostgreSQL (opcional)
* Gunicorn para despliegue
* Pillow para gestión de imágenes

### 📜 Sección de Certificados

Esta sección permite visualizar y gestionar certificados de manera eficiente:  
✔ **Filtros dinámicos** por estado y progreso.  
✔ **Acceso directo a los certificados en PDF** para descarga o revisión.  
✔ **Interfaz coherente con el diseño cyberpunk** del portafolio.  

### 🛡️ Seguridad

Este portafolio incorpora buenas prácticas de seguridad para evitar vulnerabilidades:  
✔ **Protección contra ataques CSRF** y gestión segura de sesiones.  
✔ **Restricción de acceso a archivos sensibles** para evitar accesos no autorizados.  
✔ **Validaciones robustas en formularios** para prevenir inyección de código.  
✔ **Configuración adecuada de permisos en Django Admin** para mayor control. 
✔ **Configuración segura para archivos estáticos y privados** para evitar accesos no autorizados.


### ⚙️ Instalación local

1. Clona el repositorio:

```bash
git clone https://github.com/bego46/Mi_Portafolio.git
cd Mi_Portafolio
```

2. Crea y activa un entorno virtual:

```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
```

3. Instala dependencias:

```bash
pip install -r requirements.txt
```

4. Configuración de Variables de Entorno

Antes de ejecutar el proyecto, asegúrate de **crear y configurar un archivo `.env`** dentro de la carpeta principal del repositorio. Este archivo almacenará configuraciones importantes para el sistema.

🔹 **Ejemplo de estructura en `.env`:**
```env
# 🔒 Configuración de Django
DJANGO_SECRET_KEY=tu_clave_secreta  # Reemplázalo con una clave segura
DEBUG=True  # Cambia a False en producción

# 📧 Configuración de correo SMTP
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=tu_email@gmail.com  # Ingresa tu email de envío
EMAIL_HOST_PASSWORD=tu_contraseña  # Usa una contraseña segura o un App Password
```
📌 **IMPORTANTE:** No almacenes la contraseña en el código ni en el repositorio.
Usa variables de entorno seguras o un App Password de Gmail.


5. Aplica migraciones y ejecuta el servidor:

```bash
python manage.py makemigrations  # Detecta cambios en los modelos
python manage.py migrate         # Aplica los cambios en la base de datos
python manage.py runserver       # Inicia el servidor
```

### 📝 Licencia

🔒 Este proyecto está protegido por derechos de autor.
El código contenido aquí no puede ser copiado, modificado ni reutilizado sin autorización de Developments Berlad (&lt;DB/&gt;).

### ✒️ Autor

**Developments Berlad** (&lt;DB/&gt;)
Desarrollador enfocado en crear soluciones tecnológicas útiles y atractivas.

### 📬 Contacto

* 💼 LinkedIn: [https://www.linkedin.com/in/berladgonzalez/](https://www.linkedin.com/in/berladgonzalez/)
* 📧 Email: [berlad46@gmail.com](mailto:berlad46@gmail.com)
* 🌐 Sitio web: [Próximamente](Próximamente)

---

## 🇬🇧 English  

Welcome to my personal portfolio built with Django! This project aims to showcase my skills as a web developer and highlight the projects I've worked on.

### 🚀 Features  

* Fully functional Django application.  
* Modern design with a responsive neon/cyberpunk aesthetic.  
* Project section with images and descriptions.  
* **Advanced certificate management** with dynamic filters and secure access to PDF documents.  
* Clean, modular, and well-organized code.  
* Environment variables managed via `.env`.  

### 🛠️ Technologies Used  

* Python & Django  
* HTML5, CSS3, Bootstrap (with neon customization)  
* Basic JavaScript  
* SQLite / PostgreSQL (optional)  
* Gunicorn for deployment  
* Pillow for image management  

### 📜 Certificate Section  

This section enables efficient visualization and management of certificates:  
✔ **Dynamic filters** by status and progress.  
✔ **Direct access to certificates in PDF format** for review or download.  
✔ **Consistent interface with the cyberpunk aesthetic** of the portfolio.  

### 🛡️ Security  

This portfolio implements best security practices to prevent vulnerabilities:  
✔ **Protection against CSRF attacks** and secure session management.  
✔ **Restricted access to sensitive files** to prevent unauthorized entry.  
✔ **Robust form validation** to prevent code injection.  
✔ **Proper permission configuration in Django Admin** for enhanced control.  
✔ **Secure settings for static and private files** to prevent unauthorized access.  

### ⚙️ Local Installation  

1. Clone the repository:  

```bash
git clone https://github.com/bego46/Mi_Portafolio.git
cd Mi_Portafolio
```

2. Create and activate a virtual environment:  

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:  

```bash
pip install -r requirements.txt
```

4. **Environment Variables Configuration**  

Before running the project, make sure to **create and configure a `.env` file** in the project's root directory. This file stores important system configurations.

🔹 **Example `.env` structure:**  
```env
# 🔒 Django Configuration  
DJANGO_SECRET_KEY=your_secret_key  # Replace with a secure key  
DEBUG=True  # Change to False in production  

# 📧 SMTP Email Configuration  
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend  
EMAIL_HOST=smtp.gmail.com  
EMAIL_PORT=587  
EMAIL_USE_TLS=True  
EMAIL_HOST_USER=your_email@gmail.com  # Enter your sender email  
EMAIL_HOST_PASSWORD=your_password  # Use a secure password or an App Password  
```
📌 **IMPORTANT:** Never store passwords in code or repositories.  
Use secure environment variables or an App Password for Gmail.  

5. Apply migrations and start the server:  

```bash
python manage.py makemigrations  # Detects changes in models  
python manage.py migrate         # Applies changes to the database  
python manage.py runserver       # Starts the server  
```

### 📝 License  

🔒 This project is protected by copyright.  
The code contained here **cannot be copied, modified, or reused** without authorization from Developments Berlad (&lt;DB/&gt;).  

### ✒️ Author  

**Developments Berlad** (&lt;DB/&gt;)  
Developer focused on creating **useful and visually appealing** technological solutions.  

### 📬 Contact  

* 💼 LinkedIn: [https://www.linkedin.com/in/berladgonzalez/](https://www.linkedin.com/in/berladgonzalez/)  
* 📧 Email: [berlad46@gmail.com](mailto:berlad46@gmail.com)  
* 🌐 Website: [Coming Soon](Coming Soon)  

---

## 🇩🇪 Deutsch  

Willkommen in meinem persönlichen Portfolio, das mit Django erstellt wurde! Dieses Projekt dient dazu, meine Fähigkeiten als Webentwickler zu präsentieren und meine bisherigen Projekte zu zeigen.

### 🚀 Funktionen  

* Voll funktionsfähige Django-Anwendung.  
* Modernes Design mit responsiver Benutzeroberfläche und neon/cyberpunk Ästhetik.  
* Projektbereich mit Bildern und Beschreibungen.  
* **Erweiterte Zertifikatsverwaltung** mit dynamischen Filtern und sicherem Zugriff auf PDF-Dokumente.  
* Sauberer, modularer und gut organisierter Code.  
* Verwaltung von Umgebungsvariablen mit `.env`.  

### 🛠️ Verwendete Technologien  

* Python & Django  
* HTML5, CSS3, Bootstrap (mit neon-Anpassungen)  
* Grundlegendes JavaScript  
* SQLite / PostgreSQL (optional)  
* Gunicorn für das Deployment  
* Pillow für die Bildverwaltung  

### 📜 Zertifikatsbereich  

Dieser Bereich ermöglicht eine effiziente Verwaltung und Anzeige von Zertifikaten:  
✔ **Dynamische Filter** nach Status und Fortschritt.  
✔ **Direkter Zugriff auf Zertifikate im PDF-Format** zur Überprüfung oder zum Download.  
✔ **Konsistente Benutzeroberfläche mit cyberpunk Stil** passend zum Portfolio.  

### 🛡️ Sicherheit  

Dieses Portfolio implementiert bewährte Sicherheitspraktiken, um Schwachstellen zu vermeiden:  
✔ **Schutz vor CSRF-Angriffen** und sichere Sitzungsverwaltung.  
✔ **Eingeschränkter Zugriff auf sensible Dateien**, um unautorisierte Zugriffe zu verhindern.  
✔ **Robuste Formularvalidierung**, um Code-Injektionen zu vermeiden.  
✔ **Ordnungsgemäße Berechtigungskonfiguration im Django Admin**, um die Kontrolle zu verbessern.  
✔ **Sichere Verwaltung von statischen und privaten Dateien**, um unautorisierte Zugriffe zu verhindern.  

### ⚙️ Lokale Installation  

1. Klone das Repository:  

```bash
git clone https://github.com/bego46/Mi_Portafolio.git
cd Mi_Portafolio
```

2. Erstelle und aktiviere eine virtuelle Umgebung:  

```bash
python -m venv .venv
source .venv/bin/activate  # Auf Windows: .venv\Scripts\activate
```

3. Installiere die Abhängigkeiten:  

```bash
pip install -r requirements.txt
```

4. **Konfiguration der Umgebungsvariablen**  

Bevor du das Projekt ausführst, erstelle eine **`.env` Datei** im Hauptverzeichnis des Projekts. Diese Datei speichert wichtige Systemeinstellungen.

🔹 **Beispiel für die `.env` Datei:**  
```env
# 🔒 Django Konfiguration  
DJANGO_SECRET_KEY=dein_geheimer_schlüssel  # Ersetze mit einem sicheren Schlüssel  
DEBUG=True  # In Produktion auf False setzen  

# 📧 SMTP E-Mail Konfiguration  
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend  
EMAIL_HOST=smtp.gmail.com  
EMAIL_PORT=587  
EMAIL_USE_TLS=True  
EMAIL_HOST_USER=deine_email@gmail.com  # Gib deine Absenderadresse ein  
EMAIL_HOST_PASSWORD=dein_passwort  # Nutze ein sicheres Passwort oder ein App-Passwort  
```
📌 **WICHTIG:** Speichere niemals Passwörter im Code oder Repository.  
Nutze sichere Umgebungsvariablen oder ein App-Passwort für Gmail.  

5. Wende Migrationen an und starte den Server:  

```bash
python manage.py makemigrations  # Erkennt Änderungen an den Modellen  
python manage.py migrate         # Wendet Änderungen an der Datenbank an  
python manage.py runserver       # Startet den Server  
```

### 📝 Lizenz  

🔒 Dieses Projekt ist urheberrechtlich geschützt.  
Der enthaltene Code **darf nicht kopiert, verändert oder wiederverwendet** werden ohne Genehmigung von Developments Berlad (&lt;DB/&gt;).  

### ✒️ Autor  

**Developments Berlad** (&lt;DB/&gt;)  
Entwickler mit dem Fokus auf **nützliche und visuell ansprechende technologische Lösungen**.  

### 📬 Kontakt  

* 💼 LinkedIn: [https://www.linkedin.com/in/berladgonzalez/](https://www.linkedin.com/in/berladgonzalez/)  
* 📧 E-Mail: [berlad46@gmail.com](mailto:berlad46@gmail.com)  
* 🌐 Webseite: [Demnächst verfügbar](Demnächst verfügbar)  

---


## 🇰🇷 한국어 (Korean)

Django로 만든 개인 포트폴리오에 오신 것을 환영합니다! 이 프로젝트는 웹 개발자로서의 저의 기술과 작업한 프로젝트를 보여주기 위한 것입니다.  

### 🚀 주요 특징  

* 완전히 작동하는 Django 애플리케이션  
* 반응형 디자인과 네온/사이버펑크 스타일의 인터페이스  
* 프로젝트 섹션에는 이미지 및 설명 포함  
* **고급 인증서 관리** – 동적 필터 및 PDF 문서의 안전한 접근  
* 깨끗하고 모듈화된 코드 구조  
* `.env` 파일을 통해 환경 변수 관리  

### 🛠️ 사용된 기술  

* Python & Django  
* HTML5, CSS3, Bootstrap (네온 스타일 커스텀 포함)  
* 기본적인 JavaScript  
* SQLite / PostgreSQL (선택 가능)  
* Gunicorn을 통한 배포  
* Pillow를 이용한 이미지 관리  

### 📜 인증서 섹션  

이 섹션에서는 인증서를 효과적으로 관리하고 볼 수 있습니다:  
✔ **상태 및 진행 상황에 따른 동적 필터링**  
✔ **PDF 형식 인증서를 직접 열람 및 다운로드 가능**  
✔ **포트폴리오의 사이버펑크 스타일과 일관된 UI 디자인**  

### 🛡️ 보안  

이 포트폴리오는 보안 강화를 위해 최적의 방법을 적용했습니다:  
✔ **CSRF 공격 방어 및 안전한 세션 관리**  
✔ **민감한 파일 접근 제한** – 승인되지 않은 접근 방지  
✔ **강력한 입력 검증** – 코드 삽입 공격 예방  
✔ **Django Admin에서 적절한 권한 설정** – 관리자 기능 강화  
✔ **정적 및 개인 파일의 안전한 구성** – 접근 제한 적용  

### ⚙️ 로컬 설치  

1. 저장소를 클론합니다.  

```bash
git clone https://github.com/bego46/Mi_Portafolio.git
cd Mi_Portafolio
```

2. 가상 환경을 생성하고 활성화합니다.  

```bash
python -m venv .venv
source .venv/bin/activate  # Windows 사용자는 .venv\Scripts\activate 실행
```

3. 필요한 라이브러리를 설치합니다.  

```bash
pip install -r requirements.txt
```

4. **환경 변수 설정**  

프로젝트 실행 전에 `.env` 파일을 만들어야 합니다. 이 파일에는 중요한 시스템 설정이 포함됩니다.

🔹 **`.env` 파일 예시:**  
```env
# 🔒 Django 설정  
DJANGO_SECRET_KEY=YOUR_SECRET_KEY  # 보안 키로 변경하세요  
DEBUG=True  # 프로덕션에서는 False로 변경  

# 📧 SMTP 이메일 설정  
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend  
EMAIL_HOST=smtp.gmail.com  
EMAIL_PORT=587  
EMAIL_USE_TLS=True  
EMAIL_HOST_USER=your_email@gmail.com  # 발신 이메일 주소 입력  
EMAIL_HOST_PASSWORD=your_password  # 안전한 비밀번호 또는 앱 비밀번호 사용  
```
📌 **중요:** 비밀번호를 코드나 저장소에 직접 저장하지 마세요.  
환경 변수를 안전하게 사용하거나 Gmail의 앱 비밀번호를 설정하세요.  

5. 마이그레이션을 적용하고 서버를 실행합니다.  

```bash
python manage.py makemigrations  # 모델 변경 사항 감지  
python manage.py migrate         # 데이터베이스에 변경 사항 적용  
python manage.py runserver       # 서버 시작  
```

### 📝 라이선스  

🔒 이 프로젝트는 저작권 보호를 받습니다.  
해당 코드의 **복사, 수정 및 재사용은 Developments Berlad (&lt;DB/&gt;)의 허가 없이 불가능합니다.**  

### ✒️ 개발자  

**Developments Berlad** (&lt;DB/&gt;)  
실용적이고 매력적인 **기술 솔루션을 개발하는 개발자**.  

### 📬 연락처  

* 💼 LinkedIn: [https://www.linkedin.com/in/berladgonzalez/](https://www.linkedin.com/in/berladgonzalez/)  
* 📧 이메일: [berlad46@gmail.com](mailto:berlad46@gmail.com)  
* 🌐 웹사이트: [곧 공개 예정](곧 공개 예정)  

---