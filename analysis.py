# 24f3004403@ds.study.iitm.ac.in
import marimo as mo

# --- Cell 1: Setup and Introduction ---
mo.md("# Interactive Data Analysis Demo")

# --- Cell 2: Interactive Widget ---
# This cell defines the slider. Other cells depend on its value.
slider = mo.ui.slider(start=1, stop=20, value=5, label="Select a Multiplier:")

# --- Cell 3: Data Processing (Depends on Cell 2) ---
# Data Flow: The `slider.value` from Cell 2 is used here.
multiplier = slider.value
processed_data = [x * multiplier for x in [1, 2, 3, 4, 5]]

# --- Cell 4: Dynamic Output (Depends on Cell 2 and 3) ---
# Data Flow: Displays `slider.value` (Cell 2) and `processed_data` (Cell 3).
mo.md(
    f"""
    The selected multiplier is **{slider.value}**.

    The processed data is: **`{processed_data}`**

    Visual Representation: {"🔵" * slider.value}
    """
)
