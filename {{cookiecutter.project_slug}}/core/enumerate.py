from enum import Enum


# System
class Environment(str, Enum):
    TESTING = "TESTING"
    LOCAL = "LOCAL"
    DEVELOPMENT = "DEVELOPMENT"
    PRODUCTION = "PRODUCTION"

    @property
    def is_deployed(self) -> bool:
        return self in (self.DEVELOPMENT, self.PRODUCTION)


class ResponseDataType(Enum):
    OBJECT = "Object"
    ARRAY = "Array"


# Chat
class MessageType(Enum):
    INFO = "info"
    ERROR = "error"
    SUGGEST = "suggest"
    RESTART = "restart"
    END = "end"


class ConversationStage(str, Enum):
    STAGE_1 = "stage_1"
    STAGE_2 = "stage_2"
    STAGE_3 = "stage_3"
    STAGE_4 = "stage_4"
    STAGE_5 = "stage_5"


# Expert
class ExpertSessionType(Enum):
    METHOD = ["In-Person", "Online"]
    FORMAT = ["1-2-1", "Panel", "Q&A"]


class PublishOnWebflowValue(Enum):
    LISTED = "Listed"
    UNLISTED = "Unlisted"


class ExpertSuggestionType(Enum):
    PREFERRED = "preferred"
    CHOSEN = "chosen"


class ExpertPronoun(Enum):
    MALE = "He/Him"
    FEMALE = "She/Her"
    OTHER = "They/Them"


# Prompt
class PromptSaveLocation(str, Enum):
    DB_TEMPLATE = "configs/ai_configs/db_vectorize"
    PROMPTS = "configs/ai_configs/prompts"
    SUPPORT_PROMPTS = "configs/ai_configs/support_prompts"
    ROUTER_PROMPT = "configs/ai_configs/router_prompts"
    UTTERANCE_EXAMPLES = "configs/ai_configs/utterance_examples"
    ACRONYMS = "configs/ai_configs/acronyms/"


class ExternalFolder(str, Enum):
    DB_TEMPLATE = "configs/ai_configs/db_vectorize"
    PROMPTS = "configs/ai_configs/prompts"
    SUPPORT_PROMPTS = "configs/ai_configs/support_prompts"
    ROUTER_PROMPT = "configs/ai_configs/router_prompts"
    UTTERANCE_EXAMPLES = "configs/ai_configs/utterance_examples"
    VECTORSTORE_DETAILS = "vectorstore/chroma/details_expert_db"
    ACRONYMS = "configs/ai_configs/acronyms"
    VECTORSTORE_SEARCH = "vectorstore/chroma/expert_db"


class PromptTemplate(str, Enum):
    # Vectorstore
    DB_DETAILS = "configs/ai_configs/db_vectorize/expert_details.yaml"
    DB_GENERAL = "configs/ai_configs/db_vectorize/expert.yaml"
    UTTERANCE_EXAMPLES_YAML = (
        "configs/ai_configs/utterance_examples/conversation_stage_examples.yaml"
    )

    # Main Prompt
    EXPERT_AGENT_PROMPT = "configs/ai_configs/prompts/expert_agent_prompt.yaml"
    KW_ANALYZER_PROMPT = "configs/ai_configs/prompts/kw_analyzer_prompt.yaml"
    PARALLEL_KW_ANALYZER_PROMPT = "configs/ai_configs/prompts/parallel_kw_analyzer_prompt.yaml"

    # Support Prompts
    GENERATE_EXPERT_DETAILS = "configs/ai_configs/support_prompts/generate_expert_details.yaml"
    GENERATE_QUERY_PROMPT = "configs/ai_configs/support_prompts/generate_query_prompt.yaml"
    CHOSEN_EXPERT_ANALYZER_PROMPT = (
        "configs/ai_configs/support_prompts/chosen_experts_analyer_prompt.yaml"
    )
    DETAILS_EXPERT_ANALYZER_PROMPT = (
        "configs/ai_configs/support_prompts/chosen_experts_analyer_prompt.yaml"
    )

    # Router Prompts
    STAGE_ROUTER_PROMPT = "configs/ai_configs/router_prompts/stage_router_prompt.yaml"

    # Acronym Dictionary
    ACRONYMS = "configs/ai_configs/acronyms/acronyms.yaml"


class EmbeddingModel(str, Enum):
    EMBEDDING_ADA_V2 = "text-embedding-ada-002"
    EMBEDDING_V3_LARGE = "text-embedding-3-large"
    EMBEDDING_V3_SMALL = "text-embedding-3-small"


class OpenAIModel(str, Enum):
    GPT_4_TURBO_PREVIEW = "gpt-4-turbo-preview"
    GPT_4_1106_PREVIEW = "gpt-4-1106-preview"
    GPT_4_0125_PREVIEW = "gpt-4-0125-preview"
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    GPT_3_5_TURBO_1106 = "gpt-3.5-turbo-1106"
    GPT_3_5_TURBO_0613 = "gpt-3.5-turbo-0613"
    GPT_3_5_TURBO_0125 = "gpt-3.5-turbo-0125"
