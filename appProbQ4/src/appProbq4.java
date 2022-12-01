public class appProbq4 {
    public static void main(String[] args) throws Exception {
        final int SIMNUM = 100000;
        final int HEAD = 0;
        final int TAILS = 1;
        String [] combinations = {"HHH", "HHT", "HTH", "THH", "HTT", "THT", "TTH", "TTT"};

        for(int player1Choice = 0; player1Choice < combinations.length ; player1Choice++){
            double[][] results = new double[2][8];
            for(int player2Choice = 0; player2Choice < combinations.length ; player2Choice++){
                int player1wins = 0;
                int player2wins = 0;
                char[] relevantSequence = new char[3];
                if(player1Choice != player2Choice){
                    for(int i = 0; i < SIMNUM; i++){
                        boolean winner = false;
                        while(!winner){
                            relevantSequence[0] = relevantSequence[1];
                            relevantSequence[1] = relevantSequence[2];
                            if(Math.random() < 0.5){
                                relevantSequence[2] = 'H';
                            }
                            else{
                                relevantSequence[2] = 'T';
                            }
                            String tmp = "";
                            tmp = String.copyValueOf(relevantSequence);
                            if(tmp.equals(combinations[player1Choice])){
                                player1wins++;
                                winner = true;
                                relevantSequence = new char[3];
                            }
                            if(tmp.equals(combinations[player2Choice])){
                                player2wins++;
                                winner = true;
                                relevantSequence = new char[3];
                            }
                        }
                    }
                }
                results[0][player2Choice] = player1wins;
                results[1][player2Choice] = player2wins;
            }
            int summary = 0;
            int summaryPos=0;
            System.out.println("\nPlayer 1 Choose: " + combinations[player1Choice] + ":");
            for(int b = 0; b < combinations.length; b++){
                if(results[1][b] != 0 && results[0][b] != 0){
                    System.out.println("        Player 2 with " + combinations[b] + " won with the simulated odds of " + (results[1][b]/SIMNUM) + 
                    " times, while player 1 won with the simulated odds of " + (results[0][b]/SIMNUM));
                    if(results[1][b] > summary){
                        summary = (int)results[1][b];
                        summaryPos = b;
                    }
                }
            }
            System.out.println("\nThe best strategy for Player 2 is " + combinations[summaryPos] + " if Player 1 chooses " + combinations[player1Choice] + 
            " with the simulated odds of: " +  (results[1][summaryPos]/SIMNUM) + "\n\n\n");
        }
    }
}
