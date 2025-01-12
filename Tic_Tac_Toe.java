package projekt;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Tic_Tac_Toe {
    private JFrame frame;
    private JButton[] buttons;
    private String currentPlayer;
    private String playerSymbol = "X";
    private String systemSymbol = "O";
    private boolean gameOver;

    public Tic_Tac_Toe() {
        frame = new JFrame("Tic-Tac-Toe");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 400);
        frame.setLayout(new GridLayout(3, 3));
        
        buttons = new JButton[9];
        currentPlayer = playerSymbol;
        gameOver = false;

        for (int i = 0; i < 9; i++) {
            buttons[i] = new JButton("");
            buttons[i].setFont(new Font("Arial", Font.BOLD, 36));
            buttons[i].setBackground(Color.LIGHT_GRAY);
            buttons[i].addActionListener(new ButtonClickListener(i));
            frame.add(buttons[i]);
        }

        frame.setVisible(true);
    }

    private void playerMove(int index) {
        if (buttons[index].getText().equals("") && !gameOver) {
            buttons[index].setText(playerSymbol);
            buttons[index].setForeground(Color.BLUE);
            if (checkWin(playerSymbol)) {
                endGame("Herzlichen Glückwunsch! Du hast gewonnen!", Color.GREEN);
                return;
            }
            if (checkDraw()) {
                endGame("Unentschieden! Das Spielfeld ist voll.", Color.YELLOW);
                return;
            }
            systemMove();
        }
    }

    private void systemMove() {
        for (int i = 0; i < 9; i++) {
            if (buttons[i].getText().equals("")) {
                buttons[i].setText(systemSymbol);
                buttons[i].setForeground(Color.RED);
                if (checkWin(systemSymbol)) {
                    endGame("Das System hat gewonnen! Versuch's nochmal.", Color.RED);
                }
                return;
            }
        }
        if (checkDraw()) {
            endGame("Unentschieden! Das Spielfeld ist voll.", Color.YELLOW);
        }
    }

    private boolean checkWin(String symbol) {
        // Prüfe horizontale, vertikale und diagonale Gewinnbedingungen
        return (checkLine(symbol, 0, 1, 2) || checkLine(symbol, 3, 4, 5) || checkLine(symbol, 6, 7, 8) || // Horizontal
                checkLine(symbol, 0, 3, 6) || checkLine(symbol, 1, 4, 7) || checkLine(symbol, 2, 5, 8) || // Vertikal
                checkLine(symbol, 0, 4, 8) || checkLine(symbol, 2, 4, 6));                                // Diagonal
    }

    private boolean checkLine(String symbol, int a, int b, int c) {
        return buttons[a].getText().equals(symbol) &&
               buttons[b].getText().equals(symbol) &&
               buttons[c].getText().equals(symbol);
    }

    private boolean checkDraw() {
        for (JButton button : buttons) {
            if (button.getText().equals("")) {
                return false;
            }
        }
        return true;
    }

    private void endGame(String message, Color color) {
        gameOver = true;
        JOptionPane.showMessageDialog(frame, message, "Spielende", JOptionPane.INFORMATION_MESSAGE);
        for (JButton button : buttons) {
            button.setBackground(color);
            button.setEnabled(false);
        }
        int response = JOptionPane.showConfirmDialog(frame, "Nochmal spielen?", "Neues Spiel",
                JOptionPane.YES_NO_OPTION);
        if (response == JOptionPane.YES_OPTION) {
            resetGame();
        } else {
            frame.dispose();
        }
    }

    private void resetGame() {
        for (JButton button : buttons) {
            button.setText("");
            button.setBackground(Color.LIGHT_GRAY);
            button.setEnabled(true);
        }
        gameOver = false;
        currentPlayer = playerSymbol;
    }

    private class ButtonClickListener implements ActionListener {
        private int index;

        public ButtonClickListener(int index) {
            this.index = index;
        }

        @Override
        public void actionPerformed(ActionEvent e) {
            playerMove(index);
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(Tic_Tac_Toe::new);
    }
}
