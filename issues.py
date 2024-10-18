import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

def issues():
    def load_data(folder_name="Data"):
        data_dict = {}
        for file_name in os.listdir(folder_name):
            file_path = os.path.join(folder_name, file_name)
            try:
                df = pd.read_csv(file_path, on_bad_lines='skip')
                data_dict[file_name] = df
            except pd.errors.ParserError:
                try:
                    df = pd.read_excel(file_path)
                    data_dict[file_name] = df
                except Exception as e:
                    with open(file_path, 'r') as file:
                        content = file.read()
                    df = pd.DataFrame({'content': [content]})
                    data_dict[file_name] = df
            except Exception as e:
                st.error(f"Error loading {file_name}: {str(e)}")
        return data_dict
    data_dict = load_data()
    
    st.markdown("<h1 style='text-align: center;'>SEO Issues Overview Dashboard</h1><hr style='border: 2px solid rainbow; border-radius: 5px;'>", unsafe_allow_html=True)
    st.markdown("""
    ### Data Overview
    This dashboard provides an analysis of SEO issues extracted from Screaming Frog. 
    The data represents various issues identified for different URLs from the Splashtop website, including their types, priorities, and the percentage contribution to the total SEO issues. 
    Each plot below helps to visualize different aspects of the data.
    """)

    df = data_dict.get("issues_overview_report.csv")
    st.markdown(
        """
        <style>
        h1 { text-align: center; }
        .plotly-graph-div {
            background-color: transparent !important;
        }
        </style>
        """, unsafe_allow_html=True
    )

    st.subheader("SEO Issues Data Overview",divider='rainbow')
    st.write("The table below shows the data used for the analysis.")
    st.dataframe(df) 
    st.divider()

    st.subheader("Distribution of Issue Types",divider='rainbow')
    st.write("""
    This pie chart shows the distribution of different issue types across the dataset. 
    Each slice represents the proportion of a specific issue type in relation to the total number of issues identified.
    """)

    issue_type_counts = df['Issue Type'].value_counts().reset_index()
    issue_type_counts.columns = ['Issue Type', 'Count']

    fig1 = px.pie(issue_type_counts, values='Count', names='Issue Type', 
                title='Distribution of Issue Types')
    fig1.update_traces(marker=dict(line=dict(color='#000000', width=1)))
    fig1.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

    st.plotly_chart(fig1, use_container_width=True)
    st.divider()

    st.subheader("Distribution of Issue Priority",divider='rainbow')
    st.write("""
    This pie chart provides insight into how SEO issues are prioritized. 
    It helps to understand the proportion of high, medium, and low priority issues that need attention.
    """)

    issue_priority = df['Issue Priority'].value_counts().reset_index()
    issue_priority.columns = ['Issue Priority', 'Count']
    fig2 = px.pie(issue_priority, values='Count', names='Issue Priority', 
                title='Distribution of Issue Priority')
    fig2.update_traces(marker=dict(line=dict(color='#000000', width=1)))
    fig2.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

    st.plotly_chart(fig2, use_container_width=True)
    st.divider()
    
    st.subheader("Top 10 SEO Issues by Percentage",divider='rainbow')
    st.write("""
    The bar chart below highlights the top 10 SEO issues, ranked by the percentage of their occurrence in the dataset. 
    It shows which issues are most common, allowing for focused troubleshooting.
    """)

    fig3 = px.bar(df.nlargest(10, '% of Total'), 
                x='% of Total', 
                y='Issue Name', 
                orientation='h',
                title='Top 10 SEO Issues by Percentage')
    fig3.update_layout(yaxis={'categoryorder':'total ascending'}, 
                    paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

    st.plotly_chart(fig3, use_container_width=True)
    st.divider()
    st.subheader("Sunburst Chart of SEO Issues",divider='rainbow')
    st.write("""
    This sunburst chart visualizes a hierarchical breakdown of the issues, starting from the issue type, 
    then the priority level, and finally the specific issue name. It offers a layered view of how different types of issues are distributed.
    """)

    fig4 = px.sunburst(df, 
                    path=['Issue Type', 'Issue Priority', 'Issue Name'], 
                    values='% of Total',
                    title='Sunburst Chart of SEO Issues')
    fig4.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

    st.plotly_chart(fig4, use_container_width=True)
    st.divider()