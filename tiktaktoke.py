import tkinter as tk

class TicTacToe:
    def __init__(self, root):
        self.board_width = 400
        self.board_height = 500

        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.geometry(f"{self.board_width}x{self.board_height}")
        self.root.resizable(False, False)
        self.root.configure(bg="#1E90FF")  # DodgerBlue

        self.playerX = "X"
        self.playerO = "O"
        self.currentPlayer = self.playerX

        self.turns = 0
        self.gameOver = False

        self.board = [[None for _ in range(3)] for _ in range(3)]

        self.setup_gui()

    def setup_gui(self):
        # Title label (smaller font)
        self.label = tk.Label(self.root, text=f"Tic-Tac-Toe: {self.currentPlayer}'s Turn",
                              font=("Segoe UI", 20, "bold"), fg="white", bg="#104E8B")
        self.label.pack(pady=10, fill=tk.X)

        # Game board frame
        self.board_frame = tk.Frame(self.root, bg="#1E90FF")
        self.board_frame.pack()

        for r in range(3):
            for c in range(3):
                btn = tk.Button(self.board_frame, text="", font=("Segoe UI", 30, "bold"),
                                width=4, height=1, bg="#1E90FF", fg="white",
                                bd=2, relief="ridge", command=lambda row=r, col=c: self.on_click(row, col))
                btn.grid(row=r, column=c, padx=4, pady=4)
                self.board[r][c] = btn

        # Reset button (smaller size)
        self.reset_button = tk.Button(self.root, text="Restart", font=("Segoe UI", 14, "bold"),
                                      bg="#4169E1", fg="white", padx=10, pady=5, command=self.reset_game)
        self.reset_button.pack(pady=10)

    def on_click(self, row, col):
        if self.gameOver:
            return

        btn = self.board[row][col]
        if btn["text"] == "":
            btn["text"] = self.currentPlayer
            self.turns += 1
            if self.check_winner():
                self.label.config(text=f"🎉 {self.currentPlayer} Wins!")
                self.gameOver = True
            elif self.turns == 9:
                self.show_tie()
            else:
                self.currentPlayer = self.playerO if self.currentPlayer == self.playerX else self.playerX
                self.label.config(text=f"Tic-Tac-Toe: {self.currentPlayer}'s Turn")

    def check_winner(self):
        b = self.board

        for i in range(3):
            if b[i][0]["text"] == b[i][1]["text"] == b[i][2]["text"] != "":
                self.highlight_winner(b[i][0], b[i][1], b[i][2])
                return True
            if b[0][i]["text"] == b[1][i]["text"] == b[2][i]["text"] != "":
                self.highlight_winner(b[0][i], b[1][i], b[2][i])
                return True

        if b[0][0]["text"] == b[1][1]["text"] == b[2][2]["text"] != "":
            self.highlight_winner(b[0][0], b[1][1], b[2][2])
            return True
        if b[0][2]["text"] == b[1][1]["text"] == b[2][0]["text"] != "":
            self.highlight_winner(b[0][2], b[1][1], b[2][0])
            return True

        return False

    def highlight_winner(self, b1, b2, b3):
        win_color = "#00BFFF"
        for btn in (b1, b2, b3):
            btn.config(bg=win_color)

    def show_tie(self):
        tie_color = "#87CEEB"
        for row in self.board:
            for btn in row:
                btn.config(bg=tie_color)
        self.label.config(text="😐 It's a Tie!")
        self.gameOver = True

    def reset_game(self):
        self.currentPlayer = self.playerX
        self.gameOver = False
        self.turns = 0
        self.label.config(text=f"Tic-Tac-Toe: {self.currentPlayer}'s Turn")

        for row in self.board:
            for btn in row:
                btn.config(text="", bg="#1E90FF")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
