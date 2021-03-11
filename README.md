
# NetPing Autotests

Среда выполнения автоматических тестов NetPing при использовании Selenium, SeleniumBase и Helium.

## Настрйка среды

'''sh
# Setup Python and Pip for Linux (Ubuntu)
# =======================================
# sudo apt-get update
# sudo apt-get install python3.9.2
# sudo apt-get install python3-pip

# Setup virtual environment for python modules
# ============================================

# python3 -m venv .env
# echo "USE 'source .env/bin/activate' COMMAND TO ACTIVATE VIRTUAL ENVIRONMENT."
# echo "USE 'deactivate' COMMAND TO DEACTIVATE VIRTUAL ENVIRONMENT."

# Setup SeleniumBase & Helium
# ===========================

# pip3 install seleniumbase
# pip3 install helium

# Install Selenium web drivers
# ============================

# sbase install chromedriver
# sbase install geckodriver
# seleniumbase install edgedriver   # (for Windows only)
# seleniumbase install iedriver     # (for Windows only)
# sbase install operadriver
'''

## Запуск тестов

'''sh
# Run test
# ========

# pytest test_dragn_drop_firmware.py -v     # Single test
# pytest -v                                 # All tests
'''

