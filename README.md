<h1>auto-mpg-analysis</h1>
<p>Regression analysis of Auto MPG dataset with multiple models, evaluation metrics, and results export.</p>
<h2>Project description</h2>
<p>This project:</p>
 <ol>
  <li>Downloads and cleans the <b>Auto MPG</b> dataset from the UCI Machine Learning Repository.</li>
  <li>Splits the data into training and testing sets.</li>
  <li>Builds visualizations of one-factor dependencies.</li>
  <li>
    <dl>
      <dt>Trains several models:</dt>
      <dd>Linear regression</dd>
      <dd>Polynomial regression (2nd order)</dd>
      <dd>Polynomial regression (2nd order with interactions)</dd>
    </dl>
  </li>
  <li>Calculates quality metrics (R², MSE, MAE).</li>
  <li>Saves the analysis results to a text file on the desktop with the history of runs.</li>
  <li>Builds graphs for comparing models.</li>
</ol>
<h2>Project files</h2>
<table>
  <tr>
    <th colspan="2">auto_mpg_analysis</th>
  </tr>
  <tr>
    <td>data_loader.py</td>
    <td>Loading and preprocessing data</td>
  </tr>
  <tr>
    <td>features.py</td>
    <td>Generating additional features</td>
  </tr>
  <tr>
    <td>models.py</td>
    <td>Defining and training models</td>
  </tr>
  <tr>
    <td>evaluation.py</td>
    <td>Metrics and representativeness</td>
  </tr>
  <tr>
    <td>visualization.py</td>
    <td>Plotting graphs</td>
  </tr>
  <tr>
    <td>results_calculator.py</td>
    <td>Calculating metrics for models</td>
  </tr>
  <tr>
    <td>results_saver.py</td>
    <td>Saving results to TXT</td>
  </tr>
  <tr>
    <td>main.py</td>
    <td>Running all stages of analysis</td>
  </tr>
  <tr>
    <td>README.md</td>
    <td>Project description</td>
  </tr>
</table>
<h2>Installation and launch</h2>
<ol>
  <b>
    <li>
      <dl>
        <dt>Clone the repository</dt>
        <dd>
          <code>git clone <a href>https://github.com/Kyoryuu-lab/auto-mpg-analysis/tree/main.git</a></code>
        </dd>
        <dd>
          <code>cd auto-mpg-analysis</code>
        </dd>
      </dl>
    </li>
  </b>
  <b>
    <li>
      <dl>
        <dt>Install dependencies</dt>
        <dd>
          <code>pip install pandas scikit-learn statsmodels matplotlib</code>
        </dd>
      </dl>
    </li>
  </b>
  <b>
    <li>
      <dl>
        <dt>Launch a project</dt>
        <dd>
          <code>python main.py</code>
        </dd>
      </dl>
    </li>
  </b>
</ol>
<h2>Example of console output</h2>
<samp>
  <p>
    The average value of displacement in the training sample: 196.745<br />
    The average value of displacement in the test sample:    188.996<br />
    The average value of horsepower in the training sample: 104.883<br />
    The average value of horsepower in the test sample:    103.508<br />
    [INFO] Results added to /Users/username/Desktop/auto_mpg_results.txt
  </p>
</samp>
<h2>Graph results</h2>
<p align="center">
 <img src="auto_mpg_analysis/Graphs/Displacement to MPG (Training Dataset).png" alt="Displacement to MPG" width="45%">
 <img src="auto_mpg_analysis/Graphs/Horsepower to MPG (Training Dataset).png" alt="Horsepower to MPG" width="45%">
</p>
<p align="center">
 <img src="auto_mpg_analysis/Graphs/Comparison of regression models.png" alt="Comparison of regression models" width="45%">
 <img src="auto_mpg_analysis/Graphs/Optimal model.png" alt="Optimal model" width="45%">
</p>
<h2>Example auto_mpg_results.txt file</h2>
<samp> 
  <p>
    === Test from 2025-08-13 23:20:01 ===<br />
    Model | R² | MSE | MAE<br />
    ----------------------------<br />
    Linear regression | 0.584 | 22.018 | 3.867<br />
    Polynomial (2nd order) | 0.663 | 17.853 | 3.374<br />
    Polynomial (with interaction) | 0.675 | 17.181 | 3.313
  </p>
</samp>
