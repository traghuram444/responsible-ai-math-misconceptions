import pandas as pd

from map_misconceptions.data_contract import load_training_data


def test_literal_na_is_preserved_as_a_valid_label(tmp_path) -> None:
    source = tmp_path / "train.csv"
    pd.DataFrame(
        {
            "QuestionId": ["q1"],
            "QuestionText": ["question"],
            "MC_Answer": ["answer"],
            "StudentExplanation": ["explanation"],
            "Category": ["True_Correct"],
            "Misconception": ["NA"],
        }
    ).to_csv(source, index=False)
    loaded = load_training_data(source)
    assert loaded.loc[0, "Misconception"] == "NA"
