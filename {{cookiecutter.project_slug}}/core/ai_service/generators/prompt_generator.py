import yaml
from langchain.prompts.pipeline import PipelinePromptTemplate
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts.chat import ChatPromptTemplate
from langchain_core.prompts.chat import SystemMessagePromptTemplate

from core.ai_service.generators.generator import Generator


class PromptGenerator(Generator):
    def __init__(self, yaml_file):
        with open(yaml_file, "r") as file:
            self.data = yaml.safe_load(file)

    def generate(
        self,
        name: str = "prompt",
    ) -> str:
        """Generate a string format from the given yaml file"""
        return self.data.get(name)

    def generate_prompt_template(
        self,
        name: str = "prompt",
    ) -> PromptTemplate:
        """Generate a PromptTemplate class from the given yaml file"""

        self.prompt = self.data.get(name)

        return PromptTemplate.from_template(template=self.prompt)

    def generate_chat_prompt_template(
        self,
        name: str = "prompt",
        allow_history: bool = False,
    ) -> ChatPromptTemplate:
        """Generate a PromptTemplate class from the given yaml file"""

        self.prompt = self.data.get(name)

        full_system_template = PromptTemplate.from_template(self.prompt)
        general_template = PromptTemplate.from_template(self.data.get("general_prompt"))
        input_template = PromptTemplate.from_template(self.data.get("input_prompt"))

        input_prompts = [
            ("general_prompt", general_template),
            ("input_prompt", input_template),
        ]
        pipeline_prompt = PipelinePromptTemplate(
            final_prompt=full_system_template,
            pipeline_prompts=input_prompts,
        ).format()

        template = pipeline_prompt

        human_msg_template = """{input}"""  # noqa

        input_variables = ["input"]

        if allow_history:
            human_msg_template = f"""Here is the Conversation History:\n<conversation_history>\n{{ '{{' }}conversation_history{{ '}}' }}\n</conversation_history>\n\nInput:\n<input>\n{human_msg_template}\n</input>"""  # noqa

            input_variables.append("conversation_history")

        final_prompt = ChatPromptTemplate.from_messages(
            [
                SystemMessagePromptTemplate(
                    prompt=PromptTemplate(input_variables=input_variables, template=template),
                ),
                human_msg_template,
            ],
        )

        return final_prompt
