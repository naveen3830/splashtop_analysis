import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def competitor():
    st.markdown(
        """
        <style>
        .main { 
            background-color: #FFFFFF;
            padding: 20px;
        }
        
        h1, h2, h3 { 
            color: #2c3e50;
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        }
        h1 { 
            text-align: center;
            font-size: 2.5em;
            margin-bottom: 30px;
        }
        h2 {
            font-size: 1.8em;
            margin-top: 40px;
            margin-bottom: 20px;
        }
        .stPlotlyChart {
            background-color: #FFFFFF;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            padding: 20px;
            margin-bottom: 30px;
        }
        .chart-container {
            display: flex;
            justify-content: space-between;
            align-items: stretch;
            margin-bottom: 30px;
        }
        .chart-item {
            flex: 1;
            margin: 0 10px;
        }
        </style>
        """, unsafe_allow_html=True
    )
    
    st.markdown("""
    <div style="text-align: center;">
        <h1>Splashtop Competitor Analysis Dashboard</h1>
    </div>
""", unsafe_allow_html=True)
    
    st.markdown("""
        <div style="text-align: center; font-size: 1.2em; color: #666; padding-bottom: 20px;">
            The remote desktop market has witnessed significant growth, with various players competing for market share. This analysis compares Splashtop with its top competitors.
        </div>
    """, unsafe_allow_html=True)

    data = {
        'Keyword': ['remote desktop', 'remote pc', 'go to my pc', 'teamviewer remote control', 'remote pc login', 
                    'remotepc login', 'remote desktop software', 'remote desktop programs', 'teamviewer free', 
                    'windows remote desktop'],
        'Intent': ['NT', 'I', 'NT', 'N', 'NT', 'NT', 'C', 'I', 'IT', 'I'],
        'Splashtop': [31, 14, 21, 27, 15, 24, 26, 16, 9, 46],
        'TeamViewer': [7, 6, 63, 1, 13, 39, 2, 3, 1, 31],
        'AnyViewer': [68, 94, 37, 29, 58, 48, 14, 13, 22, 76],
        'GoogleRemoteDesktop': [15, 2, 57, 59, 2, 2, 6, 9, 94, 23],
        'Volume': [74000, 18100, 9900, 8100, 6600, 6600, 5400, 4400, 4400, 4400],
        'KD%': [98, 93, 62, 69, 77, 61, 94, 84, 44, 75],
        'CPC': [3.68, 3.34, 9.94, 6.45, 1.01, 1.01, 4.66, 4.66, 2.50, 3.90],
        'Competition': [0.1, 0.08, 0.2, 0.24, 0.11, 0.11, 0.26, 0.26, 0.19, 0.11]
    }
    df = pd.DataFrame(data)
    
    def create_styled_figure(fig):
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family="Helvetica Neue, Helvetica, Arial, sans-serif", size=12, color="#2c3e50"),
            margin=dict(l=50, r=50, t=50, b=50),
            legend=dict(
                bgcolor='rgba(255,255,255,0.8)',
                bordercolor='rgba(0,0,0,0)'
            )
        )
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#E5E5E5')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#E5E5E5')
        return fig
    
    st.markdown("<h1 style='text-align: center;'>Competitor Ranking Comparison</h1><hr style='border: 2px solid rainbow; border-radius: 5px;'>", unsafe_allow_html=True)
    st.write("This bar chart compares how each competitor ranks for specific keywords. A lower ranking position is better.")

    fig1 = px.bar(df, x='Keyword', y=['Splashtop', 'TeamViewer', 'AnyViewer', 'GoogleRemoteDesktop'],
                title='Competitor Ranking Comparison', barmode='group',
                labels={'value': 'Ranking Position', 'variable': 'Competitor'},
                hover_data=['Volume', 'KD%', 'CPC'])
    fig1.update_layout(yaxis_title='Ranking Position (Lower is Better)')
    fig1 = create_styled_figure(fig1)
    st.plotly_chart(fig1, use_container_width=True)
    
    st.markdown("<h1 style='text-align: center;'>Keyword Difficulty vs. Search Volume</h1><hr style='border: 2px solid rainbow; border-radius: 5px;'>", unsafe_allow_html=True)
    
    st.write("This scatter plot visualizes the relationship between keyword difficulty (KD%) and search volume. The size of the bubbles represents the cost per click (CPC), and the color indicates the intent behind the keyword.")

    fig2 = px.scatter(df, x='KD%', y='Volume', size='CPC', color='Intent', hover_name='Keyword',
                    title='Keyword Difficulty vs. Search Volume',
                    labels={'KD%': 'Keyword Difficulty (%)', 'Volume': 'Search Volume', 'CPC': 'Cost Per Click'})
    fig2 = create_styled_figure(fig2)
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("<h1 style='text-align: center;'>Splashtop's Ranking and Market Share</h1><hr style='border: 2px solid rainbow; border-radius: 5px;'>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Splashtop's Ranking by Keyword")
        st.write("This heatmap shows Splashtop's ranking for each keyword, where a lower value indicates a higher ranking position.")
        fig3 = px.imshow(df.set_index('Keyword')[['Splashtop']], 
                        labels=dict(x="Metric", y="Keyword", color="Ranking"),
                        title="Splashtop's Ranking by Keyword")
        fig3 = create_styled_figure(fig3)
        st.plotly_chart(fig3, use_container_width=True)

    with col2:
        st.subheader("Estimated Competitor Market Share")
        st.write("This pie chart shows the estimated market share based on which competitor has the top ranking position for each keyword.")
        top_rankings = df[['Splashtop', 'TeamViewer', 'AnyViewer', 'GoogleRemoteDesktop']].apply(lambda x: x == x.min(), axis=1)
        market_share = top_rankings.sum() / len(df) * 100
        fig4 = px.pie(values=market_share, names=market_share.index, 
                    title='Estimated Market Share (Based on Top Rankings)')
        fig4 = create_styled_figure(fig4)
        st.plotly_chart(fig4, use_container_width=True)

    st.markdown("<h1 style='text-align: center;'>Keyword Intent Distribution</h1><hr style='border: 2px solid rainbow; border-radius: 5px;'>", unsafe_allow_html=True)
    st.write("This bar chart shows the distribution of keyword intents. Different types of intents (Informational, Navigational, etc.) help us understand the user's search behavior.")

    intent_counts = df['Intent'].value_counts().reset_index()
    intent_counts.columns = ['Intent', 'Count']

    fig5 = px.bar(intent_counts, x='Intent', y='Count', 
                title='Keyword Intent Distribution',
                labels={'Count': 'Number of Keywords'})
    fig5 = create_styled_figure(fig5)
    st.plotly_chart(fig5, use_container_width=True)
    
    st.markdown("<h1 style='text-align: center;'>Competitive Landscape Overview</h1><hr style='border: 2px solid rainbow; border-radius: 5px;'>", unsafe_allow_html=True)
    st.write("This overview provides insights into ranking distribution, keyword volume vs. difficulty, CPC vs. competition, and keyword intent distribution.")

    fig6 = make_subplots(rows=2, cols=2, 
                        subplot_titles=("Ranking Distribution", "Volume vs. KD%", 
                                        "CPC vs. Competition", "Intent Distribution"))
    fig6.add_trace(go.Box(y=df['Splashtop'], name='Splashtop'), row=1, col=1)
    fig6.add_trace(go.Box(y=df['TeamViewer'], name='TeamViewer'), row=1, col=1)
    fig6.add_trace(go.Box(y=df['AnyViewer'], name='AnyViewer'), row=1, col=1)
    fig6.add_trace(go.Box(y=df['GoogleRemoteDesktop'], name='Google RD'), row=1, col=1)
    fig6.add_trace(go.Scatter(x=df['KD%'], y=df['Volume'], mode='markers', 
                            text=df['Keyword'], name='Keywords'), row=1, col=2)

    # CPC vs. Competition
    fig6.add_trace(go.Scatter(x=df['Competition'], y=df['CPC'], mode='markers', 
                            text=df['Keyword'], name='Keywords'), row=2, col=1)
    fig6.add_trace(go.Bar(x=intent_counts['Intent'], y=intent_counts['Count'], name='Intent'), row=2, col=2)
    fig6.update_layout(height=800, title_text="Competitive Landscape Overview")
    fig6 = create_styled_figure(fig6)
    st.plotly_chart(fig6, use_container_width=True)