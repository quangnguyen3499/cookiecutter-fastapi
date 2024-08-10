import os
import shutil


def remove_gitlabciyml_file():
    os.remove(".gitlab-ci.yml")


def remove_github_actions():
    shutil.rmtree(".github")


def remove_bitbucket_pipeline_yml_file():
    os.remove("bitbucket-pipelines.yml")


def remove_codecommit_pipeline_yml_file():
    os.remove("buildspec.yml")


def create_dotenv_file():
    example_env_file = ".env.example"
    env_file = ".env"

    if os.path.exists(example_env_file):
        shutil.copyfile(example_env_file, env_file)
        print(f"Copied {example_env_file} to {env_file}")
    else:
        print(f"Source file {example_env_file} does not exist")


if __name__ == "__main__":
    create_dotenv_file()
    if "{{cookiecutter.ci_tool}}" != "GitLab":
        remove_gitlabciyml_file()
    if "{{cookiecutter.ci_tool}}" != "GitHub":
        remove_github_actions()
    if "{{cookiecutter.ci_tool}}" != "Bitbucket":
        remove_bitbucket_pipeline_yml_file()
    if "{{cookiecutter.ci_tool}}" != "Codecommit":
        remove_codecommit_pipeline_yml_file()
