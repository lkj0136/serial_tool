# Serial Manager Application

## 프로젝트 개요
Serial Manager Application은 다양한 시리얼 포트를 동시에 관리하고, 데이터 송수신, 파일 전송 및 포트 상태 모니터링 기능을 제공하는 GUI 기반의 응용 프로그램입니다.

## 주요 기능
- 최대 4개의 시리얼 포트 동시 관리
- 데이터 송수신 및 파일 전송
- 포트 상태 모니터링
- 설정 파일 관리
- 자동 업데이트
- 포트 상태 알림
- 자동화 스크립트
- 사용자 설정 프로필

##
SerialManagerApp/
│
├── main.py
├── README.md
├── requirements.txt
├── ui/
│   ├── main_window.py
│   ├── port_settings.py
│   ├── data_transfer.py
│   ├── file_transfer.py
│   ├── status_bar.py
│   └── profile_settings.py
│
├── models/
│   ├── serial_manager.py
│   ├── port.py
│   ├── settings.py
│   ├── automation.py
│   └── profile.py
│
├── controllers/
│   ├── main_controller.py
│   ├── port_controller.py
│   ├── data_controller.py
│   ├── file_controller.py
│   ├── automation_controller.py
│   └── profile_controller.py
│
├── views/
│   ├── main_view.py
│   ├── port_view.py
│   ├── data_view.py
│   └── file_view.py
│
├── utils/
│   ├── logger.py
│   ├── config.py
│   ├── updater.py
│   └── notification.py
│
├── resources/
│   ├── icons/
│   └── styles/
│
└── scripts/
    ├── example_script.py
    └── example_config.ini

## 설치 방법
1. 이 저장소를 클론합니다.
    ```bash
    git clone https://github.com/yourusername/SerialManagerApp.git
    ```
2. 필요한 패키지를 설치합니다.
    ```bash
    pip install -r requirements.txt
    ```
3. 프로그램을 실행합니다.
    ```bash
    python main.py
    ```

## 사용 예제
### 사용자 스크립트 예제
```python
from models.automation import AutomationScript
from models.serial_manager import SerialManager

serial_manager = SerialManager()
script = AutomationScript(serial_manager)
script.start_script(interval=5, data="Hello, World!")
