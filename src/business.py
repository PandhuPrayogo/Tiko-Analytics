import pandas as pd
import numpy as np

class Business:
    def __init__(self, df_input):
        self.df = df_input

    def get_total_engagement(self, columns: list):
        try:
            return self.df[columns].sum().sum()
        except KeyError as e:
            print(f"Error: Columns not found in DataFrame - {e}")
            return 0

    def engagement_rate(self, total_engagement: float, total_views: float):
        '''
        Engagement Rate = (Total Likes + Total Comments + Total Shares) / Total Video Views
        '''
        if total_views == 0:
            return 0.0
        return (total_engagement / total_views) * 100 # Convert to percentage

    def conversion_rate(self, profile_views: float, video_views: float):
        '''
        Conversion Rate = (Profile Views/Video Views) * 100%
        '''
        if video_views == 0:
            return 0.0
        return (profile_views / video_views) * 100

class StatusRate(Business):
    def get_account_status(self, followers_count: int, er_threshold: float = 5.0, cr_threshold: float = 1.0):
        """
        Check healthy status account
        """
        try:
            # Total video and profile views
            total_video_views = self.df['VIDEO VIEWS'].sum()
            total_profile_views = self.df['PROFILE VIEWS'].sum()

            # Total engagement
            total_engagement = self.get_total_engagement(['LIKES', 'COMMENTS', 'SHARES'])

            # Engagement and conversation rate
            engagement_rate_val = self.engagement_rate(total_engagement, total_video_views)
            conversion_rate_val = self.conversion_rate(total_profile_views, total_video_views)

            # Status analyze
            er_status = "Healthy" if engagement_rate_val >= er_threshold else "Needs Improvement"
            cr_status = "Healthy" if conversion_rate_val >= cr_threshold else "Needs Improvement"

            # Views Status
            mean_video_views = self.df['VIDEO VIEWS'].mean()
            views_status = "Excellent" if mean_video_views > followers_count else "Needs Improvement"

            # Generate KPI and OKR
            kpi_okr_strategy = self.generate_kpi_okr(
                er_status=er_status, 
                cr_status=cr_status, 
                engagement_rate=engagement_rate_val,
                video_views_mean=mean_video_views
            )

            return {
                'ACCOUNT STATUS SUMMARY': {
                    'Engagement Rate (%)': f"{engagement_rate_val:.2f}",
                    'Engagement Status': er_status,
                    'Conversion Rate (%)': f"{conversion_rate_val:.2f}",
                    'Conversion Status': cr_status,
                    'Views vs Followers Status': views_status
                }, 
                'BUSINESS STRATEGY': kpi_okr_strategy
            }
        except KeyError as e:
            print(f"Error: Missing required column - {e}")
            return None

    def generate_kpi_okr(self, er_status: str, cr_status: str, 
                        engagement_rate: float, video_views_mean: float):
        """
        Generates KPIs and OKRs based on account status.

        Returns:
            dict: Summarize KPI and OKR
        """
        strategy = {
            'KEY PERFORMANCE INDICATORS (KPI)': [],
            'OBJECTIVES AND KEY RESULTS (OKR)': []
        }

        # KPI based on Engagement Rate
        if er_status == "Healthy":
            kpi_er = f"Maintain Engagement Rate above {engagement_rate:.2f}%."
        else:
            kpi_er = "Increase Engagement Rate to 5%."
        strategy['KEY PERFORMANCE INDICATORS (KPI)'].append(kpi_er)

        # KPI based on Conversion Rate
        if cr_status == "Healthy":
            kpi_cr = "Maintain Conversion Rate above 1%."
        else:
            kpi_cr = "Increase Conversion Rate to 1%."
        strategy['KEY PERFORMANCE INDICATORS (KPI)'].append(kpi_cr)

        # Objective Key Result
        objective = "Increase audience engagement and reach through high-quality content."
        target_views_mean = np.round(video_views_mean * 1.2, 2)
        
        key_results = [
            f"Achieve an average of {target_views_mean} video views per video.",
            "Upload content consistently every 2 days."
        ]
            
        strategy['OBJECTIVES AND KEY RESULTS (OKR)'].append({
            'Objective': objective,
            'Key Results': key_results
        })

        return strategy