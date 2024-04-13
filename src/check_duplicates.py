import pandas as pd


def check_duplicates(df, columns_list):
    """
    Check for duplicates in a dataframe based on multiple sets of columns.

    Args:
    df (pd.DataFrame): The dataframe to check for duplicates.
    columns_list (list of list): List of column sets to check for duplicates.

    Returns:
    dict: A dictionary containing the number of duplicate cases and samples of duplicate rows.
    """
    results = {}

    for columns in columns_list:
        key = ', '.join(columns)
        duplicates = df[df.duplicated(subset=columns, keep=False)]
        grouped = duplicates.groupby(columns).size().reset_index(name='number_of_duplicates')
        num_duplicates = grouped['number_of_duplicates'].sum()
        results[key] = {'count': num_duplicates, 'samples': grouped}

    return results


def main():
    df = pd.DataFrame(
        data=[
            ['A', 'a', 'x', 1],
            ['A', 'b', 'x', 1],
            ['A', 'c', 'x', 1],
            ['B', 'a', 'x', 1],
            ['B', 'b', 'x', 1],
            ['B', 'c', 'x', 1],
            ['A', 'a', 'y', 1],
        ],
        columns=['col_1', 'col_2', 'col_3', 'col_4']
    )

    columns_to_check = [['col_1'], ['col_1', 'col_2'], ['col_1', 'col_2', 'col_3']]
    results = check_duplicates(df, columns_to_check)

    for key, value in results.items():
        print(f"Results for columns: {key}")
        print("Count of duplicate cases:", value['count'])
        print("Sample of duplicates:\n", value['samples'])


if __name__ == "__main__":
    main()
