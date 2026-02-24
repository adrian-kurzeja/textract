import subprocess
import os

def pytest_runtest_setup(item):
    """Debug: check environment during test setup"""
    if 'doc' in str(item.fspath):
        # Dump full env to file to check what's different
        with open('/tmp/pytest_env_dump.txt', 'w') as f:
            for k, v in sorted(os.environ.items()):
                f.write(f'{k}={v}\n')
