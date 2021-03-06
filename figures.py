import plotly.express as px
fig1 = px.bar(df1, x='Countries', y='Amount', color='Tournament', title='Amount of Majors won per country')
fig2 = px.bar(df2, x='Prize', y='Amount', color='Year', title='Major prize pool per year')
fig3 = px.scatter(df3, x='Player', y='Rating', color='Country', title='Top 10 rated players')
fig4 = px.pie(df4, values='Percentage', names='Weapons', title='Most used weapons in CSGO')
fig5 = px.box(df5, x='Teams', y='Time', title='Time as TOP#1 Team')
fig6 = px.scatter(df6, x='Weapons', y='Damage', color='Type', title='Damage per gun')
fig7 = px.scatter(df7, x='Weapons', y='Price', title='Price per weapon')
fig8 = px.treemap(df8, path=['all', 'Region', 'Teams'], values='Placement', title='Best teams in the world per region')
fig9 = px.bar(df9, x='Status', y='Money', color='Team', title='Round earnings per team and loss/win method')
