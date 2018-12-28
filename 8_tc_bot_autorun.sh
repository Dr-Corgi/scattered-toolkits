# 自动运行TC-Bot多次并保存运行结果的脚本

for i in {1..10}
do
    echo $i
    # run python script
    python run.py --agt 9 --usr 1 --max_turn 4 --movie_kb_path ./deep_dialog/data/movie_kb.1k.p --dqn_hidden_size 80 --experience_replay_pool_size 1000 --episodes 500 --simulation_epoch_size 100 --write_model_dir ./deep_dialog/checkpoints/rl_agent/ --run_mode 3 --act_level 0 --slot_err_prob 0.00 --intent_err_prob 0.00 --batch_size 16 --goal_file_path ./deep_dialog/data/user_goals_first_turn_template.part.movie.v1.p --warm_start 1 --warm_start_epochs 120
    ＃ copy the result file
    cp ./deep_dialog/checkpoints/rl_agent/agt_9_performance_records.json ./save/origin_v1_perform_$i.json
    # remove generated files
    rm ./deep_dialog/checkpoints/rl_agent/*.p
    rm ./deep_dialog/checkpoints/rl_agent/*.json
done
