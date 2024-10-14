<h1>Splashtop Content Analysis</h1>

<p>This repository contains the code and analysis for the project focused on content coverage around the phrase "Remote Access" for the website <a href="https://www.splashtop.com">www.splashtop.com</a>. The goal is to analyze keyword variations, identify gaps in competitor content, and provide insights using data analysis and visualization techniques.</p>

<h2>Project Structure</h2>

<ul>
  <li><strong>.streamlit/</strong><br>
  Contains the configuration files for the Streamlit app, including theming and layout settings.</li>
  
  <li><strong>Data/</strong><br>
  Directory that contains the datasets used for the analysis, such as scraped text data from Splashtop and its competitors.</li>
  
  <li><strong>__pycache__/</strong><br>
  Cached Python files generated during execution.</li>
  
  <li><strong>jupyter_notebooks/</strong><br>
  Contains the Jupyter notebooks used for initial data exploration and analysis before integration into the Streamlit app.</li>
  
  <li><strong>app.py</strong><br>
  The main file that runs the Streamlit application.</li>
  
  <li><strong>competitor.py</strong><br>
  Script for analyzing competitor content and identifying gaps in keyword usage.</li>
  
  <li><strong>home.py</strong><br>
  Defines the home page of the Streamlit app, displaying an overview of the analysis.</li>
  
  <li><strong>issues.py</strong><br>
  Contains code to analyze and display potential content issues or missing keyword opportunities.</li>
  
  <li><strong>requirements.txt</strong><br>
  A list of dependencies and libraries required to run the project, including Screaming Frog, Python, Streamlit, Plotly, and other data analysis tools.</li>
</ul>

<h2>How to Run</h2>

<ol>
  <li>Clone the repository:
    <pre><code>git clone https://github.com/naveen3830/splashtop_analysis.git</code></pre>
  </li>
  
  <li>Install the required dependencies:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  
  <li>Run the Streamlit application:
    <pre><code>streamlit run app.py</code></pre>
  </li>
</ol>

<h2>Tools and Libraries</h2>

<ul>
  <li><strong>Screaming Frog</strong>: For scraping content from Splashtop and its competitors.</li>
  <li><strong>Python</strong>: Used for scripting and data analysis.</li>
  <li><strong>Streamlit</strong>: For building the interactive web application.</li>
  <li><strong>Plotly</strong>: For creating visualizations.</li>
  <li><strong>Data analysis libraries</strong>: Includes libraries like Pandas and Numpy for data manipulation.</li>
</ul>

<h2>Deployment</h2>

<p>The application is deployed and accessible on Streamlit Cloud at <a href="https://splashtopanalysis.streamlit.app/">https://splashtopanalysis.streamlit.app/</a>.</p>

<h2>Contact</h2>

<p>For any questions or suggestions, please feel free to contact me.</p>
