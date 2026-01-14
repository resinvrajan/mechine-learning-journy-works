# 1. Load the CSV file using NumPy.
import numpy as np
data=np.genfromtxt("ipl_case_study\\ipl_data.csv",delimiter=",",skip_header=1,filling_values=0,dtype="str")
# 2. Find the total number of matches played.
print(data.shape)
# 3. Extract all matches played in the 2023 season.
print(data[data[:,1].astype("int")==2023])
# 4. Find the maximum and minimum runs scored by team_1.
team_1_runs=data[:,5].astype("int")
print(f"maximum {np.max(team_1_runs)} and minimum {np.min(team_1_runs)} runs scored by team_1.")
# 5. Calculate the average man_of_match_runs.
print("average man_of_match_runs",np.average(data[:,-2].astype("int")))
# 6. Count how many matches were played at Wankhede.
played_at_Wankhede=data[data[:,4]=="Wankhede"]
print("count of matches played at wankhede",played_at_Wankhede[:,0].size)
# 7. Display all matches where total_wickets > 15.
print("\n\n",data[data[:,-1].astype("int")>15])
# 8. Find matches where team_1_runs > team_2_runs.
print(data[data[:,5].astype("int")>data[:,6].astype("int")])
# 9. Calculate the average total runs per match.    
team_2_runs=data[:,6].astype("int")
print(team_2_runs)
print((team_1_runs+team_2_runs)/2)
# 10. Find how many matches CSK won.
csk_win_matches=data[data[:,7]=="CSK"]
print(f"CSK win {csk_win_matches[:,0].size} matches")
# 11. Extract matches where RCB played (either team_1 or team_2).
rcb_played_matches=data[(data[:,2]=="RCB")|(data[:,3]=="RCB")]
print(rcb_played_matches)
# 12. Find the season with the highest number of matches.
seasons=data[:,1].astype("int")
seasons_list, match_counts = np.unique(seasons, return_counts=True)
print(seasons_list)
print(match_counts)
print(seasons_list[np.argmax(match_counts)])
# 13. Get all matches where man_of_match_runs >= 75.
print(data[data[:,-2].astype("int")>=75])
# 14. Calculate the win percentage of MI.
mi_matches=data[(data[:,2]=="MI")|(data[:,3]=="MI")]
print(mi_matches[:,0].size)
mi_win=data[data[:,-3]=="MI"]
print(mi_win[:,0].size)
win_percentage_of_MI=(mi_win[:,0].size/mi_matches[:,0].size)*100
print("win percentage of MI",win_percentage_of_MI)
# 15. Find matches played between MI vs CSK.
print(data[((data[:,2]=="MI")&(data[:,3]=="CSK"))|((data[:,2]=="CSK")&(data[:,3]=="MI"))])
# 16. Find the top 5 highest scoring matches (based on total runs).
total_run_lst=data[np.argsort(team_1_runs+team_2_runs)]
print(total_run_lst[-1:-6:-1,:])






