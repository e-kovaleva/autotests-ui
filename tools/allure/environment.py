from config import settings
import sys
import platform


def create_allure_environment_file():
    items = [f'{key} = {value}' for key, value in settings.model_dump().items()]
    properties = '\n'.join(items)
    os_info = f'{platform.system()}, {platform.release()}'
    python_version = sys.version.replace('\n', ' ')

    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)
        file.write(f'\nos_info={os_info}\n')
        file.write(f'python_version={python_version}\n')
