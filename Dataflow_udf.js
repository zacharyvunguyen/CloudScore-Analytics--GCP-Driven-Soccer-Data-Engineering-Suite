function transform(line) {
    var values = line.split(',');

    // Create an object to represent a player with the new schema
    var player = {
        Player_name: values[0],
        Nationality: values[1],
        Weight: parseFloat(values[2]),
        Height: parseFloat(values[3]),
        Team: values[4],
        League: values[5],
        Appearances: parseInt(values[6]),
        Lineups: parseInt(values[7]),
        Minutes: parseInt(values[8]),
        Goals: parseInt(values[9]),
        Assists: parseInt(values[10]),
        Yellow_Cards: parseInt(values[11]),
        Red_Cards: parseInt(values[12]),
        Shots_Total: parseInt(values[13]),
        Shots_On: parseInt(values[14]),
        Passes_Total: parseInt(values[15]),
        Key_Passes: parseInt(values[16]),
        Pass_Accuracy: parseInt(values[17]),
        Tackles_Total: parseInt(values[18]),
        Blocks: parseInt(values[19]),
        Interceptions: parseInt(values[20]),
        Dribbles_Attempts: parseInt(values[21]),
        Dribbles_Success: parseInt(values[22]),
        Fouls_Drawn: parseInt(values[23]),
        Fouls_Committed: parseInt(values[24]),
        Duels_Total: parseInt(values[25]),
        Duels_Won: parseInt(values[26]),
        Penalty_Scored: parseInt(values[27]),
        Penalty_Missed: parseInt(values[28]),
        Penalty_Saved: parseInt(values[29])
    };

    var jsonString = JSON.stringify(player);
    return jsonString;
}
