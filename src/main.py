#!/usr/bin/env python3
import os

def main():
    app_name = os.getenv("APP_NAME", "SimpleApp")
    app_env = os.getenv("APP_ENV", "development")
    app_version = os.getenv("APP_VERSION", "0.0.0")
    print(f"Hello from {app_name}! Environment: {app_env}, Version: {app_version}")

if __name__ == '__main__':
    main()
