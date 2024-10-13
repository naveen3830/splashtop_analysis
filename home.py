import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import os
from pathlib import Path
from plotly.subplots import make_subplots

def home():
    def load_data(folder_name="Data"):
        data_dict = {}
        for file_name in os.listdir(folder_name):
            file_path = os.path.join(folder_name, file_name)
            try:
                # Try reading as CSV first
                df = pd.read_csv(file_path, on_bad_lines='skip')
                data_dict[file_name] = df
            except pd.errors.ParserError:
                try:
                    # If CSV fails, try reading as Excel
                    df = pd.read_excel(file_path)
                    data_dict[file_name] = df
                except Exception as e:
                    # If both fail, read as text and create a DataFrame
                    with open(file_path, 'r') as file:
                        content = file.read()
                    df = pd.DataFrame({'content': [content]})
                    data_dict[file_name] = df
            except Exception as e:
                st.error(f"Error loading {file_name}: {str(e)}")
        return data_dict

    # Load all data files
    data_dict = load_data()
        
    def splashtop_content():
        st.header("Splashtop Content Analysis", divider='rainbow')
        
        st.markdown("""
        <div class='intro'>
            <p>Welcome to the <b>Splashtop Content Analysis</b> web app! This application is designed to analyze the content coverage of Splashtop's website around the phrase <b>“Remote Access”</b> and its related keywords.</p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns([1.9, 1.2])
        
        with col1:
            st.markdown("""
            <div class='info-box'>
                <h3 class='header'>Steps Followed:</h3>
                <ol>
                    <li><b>Data Collection</b>: I used Screaming Frog application to crawl Splashtop's website and collect all page URLs.</li>
                    <li><b>Content Extraction</b>: Beautiful Soup was employed to extract textual data from each page.</li>
                    <li><b>Keyword Analysis</b>:I have analyzed the frequency of "Remote Access" and related keywords across all the extracted pages.</li>
                </ol>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <h3 class='header'>Keyword Frequency Analysis</h3>
            <p>Below is a summary of the keyword frequency analysis, showing how often each keyword or phrase appears across the pages:</p>
            """, unsafe_allow_html=True)

            # Splashtop Keyword Data
            splashtop_data = {
                'keyword': [
                    'remote access', 'remote desktop', 'virtual access', 'remote control',
                    'remote', 'remote desktop software', 'remote access solutions',
                    'virtual desktop connection', 'secure remote access', 'remote control software'
                ],
                'frequency': [614, 487, 0, 65, 4045, 62, 52, 0, 57, 1]
            }
            
            df_splashtop = pd.DataFrame(splashtop_data)
            st.dataframe(df_splashtop, use_container_width=True)

        with col2:
            st.image("https://www.splashtop.com/splashtop-logo-large.png", width=300)
            
            st.markdown("""
            <h3 class='header'>Analysis</h3>
            <p><b>Key Insights:</b></p>
            <ul>
                <li>The term <b>"remote"</b> appears most frequently, with 4045 occurrences.</li>
                <li><b>"Remote access"</b> and <b>"remote desktop"</b> are heavily used, with 614 and 487 mentions, respectively.</li>
                <li>Some keywords, such as <b>"virtual access"</b> and <b>"virtual desktop connection"</b>, have 0 occurrences, indicating a potential gap.</li>
            </ul>
            
            <p><b>Recommendations:</b></p>
            <ul>
                <li>Consider optimizing content for underused but relevant phrases like <b>"virtual access"</b> to cover more areas related to remote access solutions.</li>
            </ul>
            """, unsafe_allow_html=True)

        st.divider()
        
        st.markdown("""
        <h3 class='header'>Keyword Frequency Treemap</h3>
        This treemap visualizes the frequency of the keywords related to "Remote Access" found across Splashtop’s pages:
        """, unsafe_allow_html=True)

        fig_splashtop = px.treemap(df_splashtop, values='frequency', path=['keyword'], hover_data=['keyword', 'frequency'],
                                hover_name='keyword')
        fig_splashtop.update_layout(
            font_size=15,
            margin=dict(l=10, r=10, t=50, b=10),
            paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
            plot_bgcolor='rgba(0,0,0,0)'    # Transparent plot background
        )
        st.plotly_chart(fig_splashtop)
        st.divider()
    
        st.header("Sentiment Analysis Results", divider='rainbow')
        
        st.markdown("""
        <div class='intro'>
            <p>This section provides a comprehensive analysis of sentiment scores and readability for the URLs analyzed. Below are the key metrics such as positive, negative, and polarity scores, as well as readability metrics like the Fog Index.</p>
        </div>
        """, unsafe_allow_html=True)
        

        df_sentiment = data_dict.get("analysis_results11.csv")
        
        # Select key columns for analysis
        sentiment_columns = ['POSITIVE SCORE', 'NEGATIVE SCORE', 'POLARITY SCORE', 
                            'SUBJECTIVITY SCORE', 'FOG INDEX', 'AVG SENTENCE LENGTH',
                            'WORD COUNT', 'SYLLABLE PER WORD', 'PERSONAL PRONOUNS']

        col7, col8 = st.columns([1.9, 1.1])
        
        with col7:
            st.markdown("""
        <h3 class='header'>Sentiment Score Overview</h3>
        Below is the summary of sentiment scores for the analyzed content:
        """, unsafe_allow_html=True)
            st.dataframe(df_sentiment[sentiment_columns].describe(), use_container_width=True)
        
        with col8:
            st.markdown("<h3>Insights</h3>", unsafe_allow_html=True)
            st.write(""" 
                - **Content length:** The average word count of 772 words suggests substantial content, which search engines often favor. Longer, in-depth content tends to rank better for informational queries.
                - **Readability:** The average FOG index of 18.0393 indicates fairly complex text. For SEO, you might consider simplifying some content to improve readability and user engagement, as search engines value user experience.
                - **Sentiment analysis:** The positive sentiment (average polarity score of 0.9549) can be beneficial, as positive content often resonates better with readers and may lead to higher engagement and sharing rates.
                """)
        st.divider()   
            
        col1, col2 = st.columns([1.9, 1.1])
        with col1:
            # Positive vs Negative Scores (Graph)
            st.markdown("<h3>Positive vs Negative Sentiment</h3>", unsafe_allow_html=True)
            fig_sentiment = go.Figure()
            fig_sentiment.add_trace(go.Bar(x=df_sentiment['URL_ID'], y=df_sentiment['POSITIVE SCORE'], 
                                        name='Positive Score', marker_color='lightgreen'))
            fig_sentiment.add_trace(go.Bar(x=df_sentiment['URL_ID'], y=df_sentiment['NEGATIVE SCORE'], 
                                        name='Negative Score', marker_color='salmon'))

            fig_sentiment.update_layout(
                barmode='group',
                title="Positive vs Negative Sentiment Scores by URL",
                xaxis_title="URL ID",
                yaxis_title="Score",
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#d2d2d6')
            )
            st.plotly_chart(fig_sentiment)

        with col2:
            # Insights for Positive vs Negative Sentiment
            st.markdown("<h3>Insights</h3>", unsafe_allow_html=True)
            st.write("""
            - **Positive Content**: URLs with higher positive sentiment scores indicate user-friendly content, which can improve dwell time and user engagement.
            - **Negative Sentiment**: High negative sentiment could indicate that content needs revisiting, especially if it's critical pages like product descriptions or landing pages.
            - **Action**: We must consider rephrasing or enhancing content on URLs with high negative sentiment to improve user experience and SEO ranking.
            """)

        st.divider()

        col3, col4 = st.columns([1.9, 1.1])

        with col3:
            # Readability Metrics (Graph)
            st.markdown("<h3>Readability Metrics</h3>", unsafe_allow_html=True)
            fig_readability = go.Figure()
            fig_readability.add_trace(go.Scatter(x=df_sentiment['URL_ID'], y=df_sentiment['FOG INDEX'], 
                                                name='Fog Index', mode='lines+markers', line=dict(color='#1cb3e0')))
            fig_readability.add_trace(go.Scatter(x=df_sentiment['URL_ID'], y=df_sentiment['AVG SENTENCE LENGTH'], 
                                                name='Avg Sentence Length', mode='lines+markers', line=dict(color='#ff7f0e')))

            fig_readability.update_layout(
                title="Fog Index and Average Sentence Length by URL",
                xaxis_title="URL ID",
                yaxis_title="Score",
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#d2d2d6')
            )
            st.plotly_chart(fig_readability)

        with col4:
            # Insights for Readability Metrics
            st.markdown("<h3>Insights</h3>", unsafe_allow_html=True)
            st.write("""
            - **Fog Index**: High Fog Index indicates complex content. For SEO, simpler, easy-to-read content can rank better, especially for broader audiences.
            - **Avg Sentence Length**: Shorter sentences improve readability. Aim for a balance between brevity and clarity.
            - **Action**: We must focus on simplifying content with high Fog Index scores to improve user retention and SEO rankings.
            """)

        st.divider()

        # Further Insights on other metrics like Word Count, Personal Pronouns
        col5, col6 = st.columns([1.9, 1.1])

        with col5:
            st.markdown("<h3>Word Count Distribution</h3>", unsafe_allow_html=True)
            fig_word_count = px.histogram(df_sentiment, x='WORD COUNT', nbins=20, title='Word Count Distribution')
            fig_word_count.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#d2d2d6'))
            
            st.plotly_chart(fig_word_count)

        with col6:
            st.markdown("<h3>Insights</h3>", unsafe_allow_html=True)
            st.write("""
            - **Word Count**: Longer articles tend to perform better in search engines. If the content is too short, it may not fully satisfy user intent.
            - **Action**: We need to ensure that high-priority URLs have adequate word counts to match the competition, especially for more competitive keywords.
            """)
            
        st.divider()



    def anydesk_content():
        st.header("AnyDesk Content Analysis", divider='rainbow')

        st.markdown("""
            <div class='intro'>
                <p>This page provides an in-depth analysis of <b>AnyDesk's</b> content, a major competitor to <b>Splashtop</b>, with a focus on <b>Remote Access</b> and related topics.</p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div style="text-align: center;">
                <img src="https://img.swapcard.com/?u=https%3A%2F%2Fcdn-api.swapcard.com%2Fpublic%2Fimages%2Fbac2e0339ab54511aaf8e3f7fe1e6269.png&q=0.8&m=fit&w=400&h=200" width="300">
            </div>
        """, unsafe_allow_html=True)
        st.divider()

        col1, col2 = st.columns([1.9, 1.2])

        with col1:
            st.markdown("""
            <h3 class='header'>Keyword Frequency Analysis</h3>
            <p>Below is a summary of the keyword frequency analysis, showing how often each keyword or phrase appears across the pages:</p>
            """, unsafe_allow_html=True)

            # AnyDesk Keyword Data
            anydesk_data = {
                'keyword': [
                    'remote access', 'remote desktop', 'virtual access', 'remote control',
                    'remote', 'remote desktop software', 'remote access solutions',
                    'virtual desktop connection', 'secure remote access', 'remote control software'
                ],
                'frequency': [354, 403, 0, 18, 1973, 65, 0, 0, 7, 0]
            }

            df_anydesk = pd.DataFrame(anydesk_data)
            st.dataframe(df_anydesk, use_container_width=True)

        with col2:
            st.markdown("""
            <h3 class='header'>Analysis Report</h3>
            <p><b>Key Insights:</b></p>
            <ul>
                <li>The term <b>"remote"</b> appears most frequently, with 1973 occurrences.</li>
                <li><b>"Remote desktop"</b> and <b>"remote access"</b> are also significant, with 403 and 354 mentions, respectively.</li>
                <li>Some keywords, such as <b>"virtual access"</b> and <b>"virtual desktop connection"</b>, have 0 occurrences, indicating a gap in coverage.</li>
            </ul>
            
            <p><b>Recommendations:</b></p>
            <ul>
                <li>Consider enhancing content for secure remote access and expanding coverage on "virtual access".</li>
            </ul>
            """, unsafe_allow_html=True)

        st.divider()

        st.markdown("""
        <h3 class='header'>Keyword Frequency Treemap</h3>
        This treemap visualizes the frequency of the keywords related to "Remote Access" found across AnyDesk’s pages:
        """, unsafe_allow_html=True)

        fig_anydesk = px.treemap(df_anydesk, values='frequency', path=['keyword'], hover_data=['keyword', 'frequency'],
                                hover_name='keyword')
        fig_anydesk.update_layout(
            font_size=15,
            margin=dict(l=10, r=10, t=50, b=10),
            paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
            plot_bgcolor='rgba(0,0,0,0)'    # Transparent plot background
        )
        st.plotly_chart(fig_anydesk, key="treemap_chart")

        st.divider()
        st.header("Sentiment Analysis Results", divider='rainbow')

        st.markdown("""
        <div class='intro'>
            <p>This section provides a comprehensive analysis of sentiment scores and readability for the URLs analyzed. Below are the key metrics such as positive, negative, and polarity scores, as well as readability metrics like the Fog Index.</p>
        </div>
        """, unsafe_allow_html=True)

        df_sentiment = data_dict.get("analysis_results12.csv")

        # Select key columns for analysis
        sentiment_columns = ['POSITIVE SCORE', 'NEGATIVE SCORE', 'POLARITY SCORE', 
                            'SUBJECTIVITY SCORE', 'FOG INDEX', 'AVG SENTENCE LENGTH',
                            'WORD COUNT', 'SYLLABLE PER WORD', 'PERSONAL PRONOUNS']

        # Further Insights on other metrics like Word Count, Personal Pronouns
        col7, col8 = st.columns([1.9, 1.1])

        with col7:
            st.markdown("""
        <h3 class='header'>Sentiment Score Overview</h3>
        Below is the summary of sentiment scores for the analyzed content:
        """, unsafe_allow_html=True)
            st.dataframe(df_sentiment[sentiment_columns].describe(), use_container_width=True)
        
        with col8:
            st.markdown("<h3>Insights</h3>", unsafe_allow_html=True)
            st.write(""" 
                - The analysis covers 109 content items across various linguistic and stylistic measures.
                - On average, the content has a strong positive sentiment (mean polarity score of 0.9745) and moderate complexity (average FOG index of 14.5885).
                - The average word count is 982.9725 words per item, with significant variation (from 4 to 9,051 words).
                """)

        st.divider()

        col1, col2 = st.columns([1.9, 1.1])

        with col1:
            st.markdown("<h3>Positive vs Negative Sentiment</h3>", unsafe_allow_html=True)
            fig_sentiment = go.Figure()
            fig_sentiment.add_trace(go.Bar(x=df_sentiment['URL_ID'], y=df_sentiment['POSITIVE SCORE'], 
                                        name='Positive Score', marker_color='lightgreen'))
            fig_sentiment.add_trace(go.Bar(x=df_sentiment['URL_ID'], y=df_sentiment['NEGATIVE SCORE'], 
                                        name='Negative Score', marker_color='salmon'))

            fig_sentiment.update_layout(
                barmode='group',
                title="Positive vs Negative Sentiment Scores by URL",
                xaxis_title="URL ID",
                yaxis_title="Score",
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#d2d2d6')
            )
            st.plotly_chart(fig_sentiment, key="sentiment_bar_chart")

        with col2:
            st.markdown("<h3>Insights</h3>", unsafe_allow_html=True)
            st.write("""
            - **Positive Content**: URLs with higher positive sentiment scores indicate user-friendly content, which can improve dwell time and user engagement.
            - **Negative Sentiment**: High negative sentiment could indicate that content needs revisiting, especially if it's critical pages like product descriptions or landing pages.
            - **Action**: We must consider rephrasing or enhancing content on URLs with high negative sentiment to improve user experience and SEO ranking.
            """)

        st.divider()

        col3, col4 = st.columns([1.9, 1.1])

        with col3:
            st.markdown("<h3>Readability Metrics</h3>", unsafe_allow_html=True)
            fig_readability = go.Figure()
            fig_readability.add_trace(go.Scatter(x=df_sentiment['URL_ID'], y=df_sentiment['FOG INDEX'], 
                                                name='Fog Index', mode='lines+markers', line=dict(color='#1cb3e0')))
            fig_readability.add_trace(go.Scatter(x=df_sentiment['URL_ID'], y=df_sentiment['AVG SENTENCE LENGTH'], 
                                                name='Avg Sentence Length', mode='lines+markers', line=dict(color='#ff7f0e')))

            fig_readability.update_layout(
                title="Fog Index and Average Sentence Length by URL",
                xaxis_title="URL ID",
                yaxis_title="Score",
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#d2d2d6')
            )
            st.plotly_chart(fig_readability, key="readability_chart")

        with col4:
            st.markdown("<h3>Insights</h3>", unsafe_allow_html=True)
            st.write("""
            - **Fog Index**: High Fog Index indicates complex content. For SEO, simpler, easy-to-read content can rank better, especially for broader audiences.
            - **Avg Sentence Length**: Shorter sentences improve readability. Aim for a balance between brevity and clarity.
            - **Action**: We must focus on simplifying content with high Fog Index scores to improve user retention and SEO rankings.
            """)

        st.divider()

        col5, col6 = st.columns([1.9, 1.1])

        with col5:
            st.markdown("<h3>Word Count Distribution</h3>", unsafe_allow_html=True)
            fig_word_count = px.histogram(df_sentiment, x='WORD COUNT', nbins=20, title='Word Count Distribution')
            fig_word_count.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#d2d2d6')
            )
            st.plotly_chart(fig_word_count, key="word_count_histogram")

        with col6:
            st.markdown("<h3>Insights</h3>", unsafe_allow_html=True)
            st.write("""
            - **Word Count**: Longer articles tend to perform better in search engines. If the content is too short, it may not fully satisfy user intent.
            - **Action**: We need to ensure that high-priority URLs have adequate word counts to match the competition, especially for more competitive keywords.
            """)

        st.divider()

    def comparison():
        st.header("Splashtop vs AnyDesk: A Content Comparison",divider='rainbow')

        # Mock data for keyword frequencies (replace these with actual data)
        splashtop_keywords = {
            'remote access': 614,
            'remote desktop': 487,
            'virtual access': 0,
            'remote control': 65,
            'remote': 4045,
            'remote desktop software': 62,
            'remote access solutions': 52,
            'virtual desktop connection': 0,
            'secure remote access': 57,
            'remote control software': 1
        }
        
        anydesk_keywords = {
            'remote access': 310,
            'remote desktop': 456,
            'virtual access': 20,
            'remote control': 70,
            'remote': 2900,
            'remote desktop software': 80,
            'remote access solutions': 30,
            'virtual desktop connection': 10,
            'secure remote access': 60,
            'remote control software': 5
        }
        
        col1, col2 = st.columns([1.3, 1.7])
        
        with col1:
            st.markdown("<h3>Keyword Frequency Table</h3>", unsafe_allow_html=True)
            df_keywords = pd.DataFrame({
                'Keyword': splashtop_keywords.keys(),
                'Splashtop': splashtop_keywords.values(),
                'AnyDesk': anydesk_keywords.values()
            })
            st.dataframe(df_keywords, use_container_width=True)
            
        with col2:
            st.markdown("<h3>Keyword Frequency Chart</h3>", unsafe_allow_html=True)
            fig = go.Figure(data=[
                go.Bar(name='Splashtop', x=list(splashtop_keywords.keys()), y=list(splashtop_keywords.values())),
                go.Bar(name='AnyDesk', x=list(anydesk_keywords.keys()), y=list(anydesk_keywords.values()))
            ])
            fig.update_layout(barmode='group', height=500, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
        - **Splashtop** uses keywords like 'remote access' and 'remote' more often.
        - **AnyDesk** focuses more on 'remote desktop' and 'remote desktop software'.
        - Splashtop could benefit by strengthening content around 'remote desktop'.
        """)

        st.divider()

        # Content Metrics Comparison (add your metrics data here)
        splashtop_metrics = {
            'Word Count': 25000,
            'Fog Index': 18.04,
            'Reading Time (min)': 15
        }
        
        anydesk_metrics = {
            'Word Count': 20000,
            'Fog Index': 14.25,
            'Reading Time (min)': 12
        }

        col3, col4 = st.columns([1.5, 1.5])
        with col3:
            st.markdown("<h3>Content Metrics Table</h3>", unsafe_allow_html=True)
            df_metrics = pd.DataFrame({
                'Metric': splashtop_metrics.keys(),
                'Splashtop': splashtop_metrics.values(),
                'AnyDesk': anydesk_metrics.values()
            })
            st.dataframe(df_metrics, use_container_width=True)

        with col4:
            st.markdown("<h3>Key Insights from Metrics</h3>", unsafe_allow_html=True)
            st.markdown("""
            - **AnyDesk** has longer content on average, which can improve ranking for in-depth queries.
            - **Splashtop** has more complex content, indicated by the higher Fog Index. Simplifying some content could boost readability.
            - **Action**: Expanding content and simplifying readability may help Splashtop compete better.
            """)

        st.divider()

        col5, col6 = st.columns([1.5, 1.5])
        with col5:
            st.markdown("<h3>Readability and Complexity</h3>", unsafe_allow_html=True)
            st.markdown("""
            - **Splashtop** has higher complexity (18.04 Fog Index), meaning its content is harder to read.
            - **Action**: Simplifying the language could help make the content more accessible to a wider audience.
            """)

        with col6:
            st.markdown("<h3>Engagement through Personal Pronouns</h3>", unsafe_allow_html=True)
            st.markdown("""
            - **AnyDesk** uses more personal pronouns, which may create a more engaging, conversational tone.
            - **Action**: Splashtop could benefit from a more conversational tone to enhance reader engagement.
            """)

        st.divider()

        col7, col8 = st.columns([1.5, 1.5])
        with col7:
            st.markdown("<h3>Content Volume</h3>", unsafe_allow_html=True)
            st.markdown("""
            - **Splashtop** has more content overall, which is great for maintaining its presence.
            - **Action**: Keep producing a wide variety of content to stay ahead.
            """)

        with col8:
            st.markdown("<h3>Sentiment Analysis</h3>", unsafe_allow_html=True)
            st.markdown("""
            - Both companies maintain a very positive sentiment.
            - **Action**: Continue to optimize content for positive user engagement.
        """)
        
        st.divider()

    st.title("Remote Access Content Analysis")

    tab1, tab2, tab3= st.tabs(["Splashtop Analysis", "AnyDesk Analysis","Comparison"])

    with tab1:
        splashtop_content()

    with tab2:
        anydesk_content()
        
    with tab3:
        comparison()
