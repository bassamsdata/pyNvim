import numpy as np
import pandas as pd
from lets_plot import *

LetsPlot.setup_html()  # Or LetsPlot.setup_show() depending on your environment

# 1. Generate sample data
np.random.seed(42)  # for reproducibility
n_points = 50
data = {
    "x_values": np.random.rand(n_points) * 10,
    "y_values": 2 * np.random.rand(n_points) * 10 + np.random.randn(n_points) * 2,
    "category": np.random.choice(["A", "B", "C"], n_points),
}

# 2. Create a pandas DataFrame
df = pd.DataFrame(data)

# 3. Create a plot using lets-plot
p = (
    ggplot(df, aes(x="x_values", y="y_values", color="category"))
    + geom_point(size=3, alpha=0.7)
    + ggtitle("Sample Scatter Plot with Lets-Plot")
    + xlab("X Value")
    + ylab("Y Value")
    + theme_minimal()
)

# 4. Display or save the plot
# p.show() # Use this in interactive environments like Jupyter
ggsave(p, "sample_plot.png", dpi=300)  # Saves the plot to a file

print("Pandas DataFrame head:")
print(df.head())
print("\nPlot saved as 'sample_plot.png'")
