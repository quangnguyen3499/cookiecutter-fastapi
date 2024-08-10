import argparse
import os

from core.constants import BASE_DIR
from core.utils.load_utils import load_yaml_template
from core.utils.openai_utils import format_csv_to_openai_training_data


def setup_arguments():
    # Create the parser
    parser = argparse.ArgumentParser(description="Generate the training data from given csv")

    # Add the arguments
    parser.add_argument(
        "--raw_data_path",
        default=os.path.join(BASE_DIR, "data/openai/raw/raw_tone_of_voice.csv"),
        help="The path to the raw data (default: data/openai/raw/raw_tone_of_voice.csv)",
    )

    # Add the arguments
    parser.add_argument(
        "--output_path",
        default=os.path.join(BASE_DIR, "data/openai/training/training_tone_of_voice.jsonl"),
        help="The path to the generated training data (default: data/openai/training/training_tone_of_voice.jsonl)",
    )

    return parser.parse_args()


def main():
    args = setup_arguments()

    data_dict = load_yaml_template(
        os.path.join(BASE_DIR, "configs/ai_configs/support_prompts/format_chatbot_output.yaml"),
    )

    system_msg = data_dict["prompt"]

    format_csv_to_openai_training_data(
        csv_path=args.raw_data_path,
        system_message=system_msg,
        output_path=args.output_path,
    )


if __name__ == "__main__":
    main()
