import plotly.express as px

def create_histogram(dataframe, attribute_col, x_label, color_map):
    """
    Generates a grouped histogram showing survival counts for a given attribute.

    Args:
        dataframe (pd.DataFrame): The input data
        attribute_col (str): The column name to use for the x-axis
        x_label (str): The human-readable label for the x-axis
        color_map (dict): A dictionary defining discrete colors for 'survived'

    Returns:
        plotly.graph_objects.Figure: The generated histogram figure.
    """
    
    if attribute_col == "class":
        class_order = ["First", "Second", "Third"]
        category_orders = {"class": class_order}
    else: 
        category_orders = None

    plot_title = f"Survival Count by {x_label}"

    fig = px.histogram(
        dataframe,
        x=attribute_col,
        color="survived",
        barmode="group",
        text_auto=True, 
        title=plot_title,
        labels={"sex": x_label, "survived": "Survived"},
        category_orders=category_orders,
        color_discrete_map=color_map
    )
    return fig


def box_hist_violin(dataframe):
    """
    Generates an age distribution histogram with an integrated marginal box plot.

    Args:
        dataframe (pd.DataFrame): The input data containing 'age' and 'class'.

    Returns:
        plotly.graph_objects.Figure: The generated histogram figure.
    """
    fig = px.histogram(
        dataframe,
        x="age",
        color="class",
        marginal="box",
        title="Age Distribution",
        labels={"age": "Age", "class": "Passenger Class"}, 
    )
    return fig