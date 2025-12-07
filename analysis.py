import marimo

__generated_with = "0.8.0"
app = marimo.App()

@app.cell
def _():
    import marimo as mo
    
    # Author Email: 24f3001410@ds.study.iitm.ac.in
    # This notebook demonstrates interactive data flow between cells.
    return mo,


@app.cell
def _(mo):
    # CELL 1: Interactive Input
    # We create a slider widget here. This acts as the source of our data flow.
    # Changing this slider will automatically trigger updates in dependent cells.
    factor_slider = mo.ui.slider(start=1, end=10, step=0.5, label="Multiplication Factor")
    
    # Display the slider
    factor_slider
    return factor_slider,


@app.cell
def _(factor_slider):
    # CELL 2: Data Processing (Dependent on Cell 1)
    # This cell takes the value from 'factor_slider' in the previous cell.
    # DATA FLOW: Widget State -> Variable Calculation
    
    base_value = 100
    current_factor = factor_slider.value
    
    # Calculate the result based on the interactive input
    calculated_result = base_value * current_factor
    return base_value, calculated_result, current_factor


@app.cell
def _(base_value, calculated_result, current_factor, mo):
    # CELL 3: Dynamic Visualization (Dependent on Cell 2)
    # This cell takes the calculated variables and renders Markdown.
    # DATA FLOW: Calculated Variables -> Dynamic UI Output
    
    mo.md(
        f"""
        ### Dynamic Analysis Report
        
        We are analyzing the impact of the factor on a base value of **{base_value}**.
        
        * **Selected Factor:** {current_factor}
        * **Result:** {calculated_result}
        
        ---
        *As you move the slider above, this text updates in real-time.*
        """
    )
    return


if __name__ == "__main__":
    app.run()
