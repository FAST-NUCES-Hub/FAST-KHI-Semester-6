# HOW.md — Technical Implementation Reference

> **Chess Project with Five Queens Mode**  
> A 3D chess game built in C/C++ using Raylib, featuring a custom Minimax AI engine, Stockfish integration, and a bespoke Five Queens variant designed for an AI lab project.

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Project Structure](#2-project-structure)
3. [Libraries and Dependencies](#3-libraries-and-dependencies)
   - 3.1 [Raylib](#31-raylib)
   - 3.2 [raygui](#32-raygui)
   - 3.3 [subprocess.h](#33-subprocessh)
   - 3.4 [Stockfish Engine](#34-stockfish-engine)
4. [Architecture Overview](#4-architecture-overview)
   - 4.1 [Class Hierarchy](#41-class-hierarchy)
   - 4.2 [Game State Machine](#42-game-state-machine)
5. [Settings System (`Settings.h`)](#5-settings-system-settingsh)
   - 5.1 [Static Members](#51-static-members)
   - 5.2 [Binary Serialization](#52-binary-serialization)
   - 5.3 [Forward Compatibility](#53-forward-compatibility)
6. [Chess Piece Representation (`ChessPiece.cpp/.h`)](#6-chess-piece-representation-chesspiececpph)
   - 6.1 [Piece Types](#61-piece-types)
   - 6.2 [3D Model Loading](#62-3d-model-loading)
   - 6.3 [Bounding Box System](#63-bounding-box-system)
7. [Board Spot System (`Spot.cpp/.h`)](#7-board-spot-system-spotcpph)
8. [Piece Selection System (`SelectedPiece.cpp/.h`)](#8-piece-selection-system-selectedpiececpph)
9. [Board Logic (`Board.cpp/.h`)](#9-board-logic-boardcpph)
   - 9.1 [Board Initialization — Async Loading](#91-board-initialization--async-loading)
   - 9.2 [DrawBoard — Render Loop](#92-drawboard--render-loop)
   - 9.3 [Move Animation System](#93-move-animation-system)
   - 9.4 [Selecter — Raycasting Input](#94-selecter--raycasting-input)
   - 9.5 [Legal Move Highlighting](#95-legal-move-highlighting)
   - 9.6 [MakeMove and DoMove](#96-makemove-and-domove)
   - 9.7 [UpdateChessboard — FEN Sync](#97-updatechessboard--fen-sync)
   - 9.8 [Pawn Promotion](#98-pawn-promotion)
   - 9.9 [Undo/Redo System](#99-undoredo-system)
   - 9.10 [Save, Load, and PGN Export](#910-save-load-and-pgn-export)
   - 9.11 [Win Detection](#911-win-detection)
10. [AI Engine Interface (`IChessEngine.h`)](#10-ai-engine-interface-ichessengineh)
11. [Minimax Engine (`MinimaxEngine.cpp/.h`)](#11-minimax-engine-minimaxenginecpph)
    - 11.1 [Internal Board Representation](#111-internal-board-representation)
    - 11.2 [Move Representation](#112-move-representation)
    - 11.3 [Pseudo-Legal Move Generation](#113-pseudo-legal-move-generation)
    - 11.4 [Legal Move Filtering](#114-legal-move-filtering)
    - 11.5 [Apply and Undo Move (MoveUndo)](#115-apply-and-undo-move-moveundo)
    - 11.6 [Static Evaluation Function](#116-static-evaluation-function)
    - 11.7 [Piece-Square Tables](#117-piece-square-tables)
    - 11.8 [Minimax with Alpha-Beta Pruning](#118-minimax-with-alpha-beta-pruning)
    - 11.9 [Move Ordering Optimization](#119-move-ordering-optimization)
    - 11.10 [Win/Stalemate Detection](#1110-winstalemate-detection)
    - 11.11 [FEN Loading and Extraction](#1111-fen-loading-and-extraction)
12. [Stockfish Engine Integration (`Stockfish.cpp/.h`)](#12-stockfish-engine-integration-stockfishcpph)
    - 12.1 [Process Management via subprocess.h](#121-process-management-via-subprocessh)
    - 12.2 [UCI Communication Protocol](#122-uci-communication-protocol)
    - 12.3 [Legal Move Query via Perft](#123-legal-move-query-via-perft)
    - 12.4 [Board State Extraction](#124-board-state-extraction)
    - 12.5 [Win Detection via Stockfish](#125-win-detection-via-stockfish)
    - 12.6 [Best Move and Evaluation](#126-best-move-and-evaluation)
    - 12.7 [Starting FEN Support](#127-starting-fen-support)
13. [Five Queens Mode — Complete Implementation](#13-five-queens-mode--complete-implementation)
    - 13.1 [Concept and Design Goals](#131-concept-and-design-goals)
    - 13.2 [FEN Generation Algorithm (`GenerateFiveQueensFen`)](#132-fen-generation-algorithm-generatefivequeensfen)
    - 13.3 [Integration with the Game Loop](#133-integration-with-the-game-loop)
    - 13.4 [Compatibility with Both Engines](#134-compatibility-with-both-engines)
    - 13.5 [Implications for Gameplay](#135-implications-for-gameplay)
14. [Main Entry Point (`ChessProject.cpp`)](#14-main-entry-point-chessprojectcpp)
    - 14.1 [Window and Camera Initialization](#141-window-and-camera-initialization)
    - 14.2 [Game State Loop](#142-game-state-loop)
    - 14.3 [Loading Screen State](#143-loading-screen-state)
    - 14.4 [Menu Screen State](#144-menu-screen-state)
    - 14.5 [Game Screen State](#145-game-screen-state)
    - 14.6 [Pause Screen State](#146-pause-screen-state)
    - 14.7 [Promotion Screen State](#147-promotion-screen-state)
    - 14.8 [Winning Screen State](#148-winning-screen-state)
    - 14.9 [File Selection Screen State](#149-file-selection-screen-state)
    - 14.10 [Settings Screen State](#1410-settings-screen-state)
    - 14.11 [Evaluation Bar and Move History HUD](#1411-evaluation-bar-and-move-history-hud)
15. [Frontend and GUI System](#15-frontend-and-gui-system)
    - 15.1 [raygui Immediate-Mode GUI](#151-raygui-immediate-mode-gui)
    - 15.2 [MenuLayout.h — Main Menu](#152-menulayouth--main-menu)
    - 15.3 [Options.h — Settings Screen](#153-optionsh--settings-screen)
    - 15.4 [gui_window_file_dialog.h — File Browser](#154-gui_window_file_dialogh--file-browser)
    - 15.5 [UI Themes and Style System](#155-ui-themes-and-style-system)
16. [3D Camera System](#163d-camera-system)
17. [Coordinate System and Board Mapping](#17-coordinate-system-and-board-mapping)
18. [Build System and Project Configuration](#18-build-system-and-project-configuration)
19. [Data Flow Diagram](#19-data-flow-diagram)
20. [Known Limitations and Design Notes](#20-known-limitations-and-design-notes)

---

## 1. Project Overview

This project is a fully functional 3D chess game written in **C and C++**, using **Raylib** for 3D rendering and window management, and **raygui** for the immediate-mode graphical user interface. The game supports two AI backends — a custom hand-written **Minimax engine with alpha-beta pruning**, and the industry-standard **Stockfish** engine communicated with over a subprocess pipe.

The defining feature is **Five Queens Mode**, a custom game variant designed for an AI lab project. In this mode, each side begins with two queens instead of one, and an additional fifth queen (belonging randomly to white or black) is placed at a random position in the middle four rows of the board. This creates a significantly more tactically complex starting position that exercises the AI engine's move evaluation and pruning mechanisms under materially unbalanced conditions.

All game settings — board colors, piece model paths, theme selection, engine choice, and the Five Queens toggle — are persisted to a binary file (`Settings.bin`) and loaded on startup.

---

## 2. Project Structure

```
ChessProject-feature-five-queens-mode/
│
├── README.md                          # Basic project description
│
└── ChessProject/
    ├── ChessProject.sln               # Visual Studio solution file
    ├── ChessProject.vcxproj           # MSVC project configuration
    │
    ├── ChessProject.cpp               # ★ Main entry point — game loop, state machine
    │
    ├── Board.h / Board.cpp            # ★ Core board logic, move execution, animation
    ├── ChessPiece.h / ChessPiece.cpp  # 3D piece representation and model loading
    ├── Spot.h / Spot.cpp              # Individual board square (cell) logic
    ├── SelectedPiece.h / SelectedPiece.cpp  # Piece selection and highlight state
    │
    ├── IChessEngine.h                 # ★ Abstract engine interface (pure virtual)
    ├── MinimaxEngine.h / MinimaxEngine.cpp  # ★ Custom Minimax AI with alpha-beta
    ├── Stockfish.h / Stockfish.cpp    # ★ Stockfish subprocess communication
    │
    ├── MainMenu.h / MainMenu.cpp      # Legacy menu class (superseded by raygui layout)
    ├── Settings.h                     # ★ Global settings singleton with binary I/O
    │
    ├── gui_Settings.h                 # raygui settings panel helpers
    ├── gui_window_file_dialog.h       # raygui file browser dialog
    │
    ├── game.pgn                       # Sample exported PGN file
    ├── savegame.dat                   # Sample saved game data
    │
    ├── Resources/
    │   ├── ChessSet/                  # (gitignored) .glb 3D model files for pieces
    │   └── GUI/
    │       ├── MenuLayout.h           # raygui-generated main menu layout
    │       └── Options.h             # raygui-generated options screen layout
    │
    └── styles/                        # raygui theme style packs
        ├── default/                   # Default light theme
        ├── ashes/                     # Dark-grey "ashes" theme
        ├── bluish/                    # Blue-toned theme
        ├── candy/                     # Pastel "candy" theme
        ├── cherry/                    # Red "cherry" theme
        ├── cyber/                     # Neon "cyber" theme
        └── dark/                      # Dark theme
```

**Key file roles:**

| File | Responsibility |
|------|---------------|
| `ChessProject.cpp` | Application entry, window, camera, state machine |
| `Board.cpp/.h` | Game state, move execution, sync with engine |
| `IChessEngine.h` | Polymorphic engine contract |
| `MinimaxEngine.cpp/.h` | Self-contained chess AI (no external process) |
| `Stockfish.cpp/.h` | Subprocess wrapper for Stockfish UCI protocol |
| `Settings.h` | All global configuration — persisted to disk |
| `Board.cpp :: GenerateFiveQueensFen()` | Five Queens Mode FEN construction |

---

## 3. Libraries and Dependencies

### 3.1 Raylib

**Raylib** is a simple, easy-to-use C library for videogame programming. It wraps OpenGL and provides functions for:

- **Window management** — `InitWindow`, `CloseWindow`, `SetTargetFPS`
- **3D rendering** — `BeginMode3D`, `EndMode3D`, `DrawModel`, `DrawCube`, `DrawGrid`
- **Camera** — `Camera3D` struct, `UpdateCamera`
- **Input** — `IsMouseButtonPressed`, `GetMouseRay`, `IsKeyPressed`, `IsCursorHidden`
- **Ray collision** — `GetRayCollisionBox` for picking board squares via mouse
- **Model loading** — `LoadModel` for `.glb` files, `UnloadModel`
- **Math** — `Vector3Lerp` for animation interpolation, via `raymath.h`
- **Random** — `GetRandomValue` (used in Five Queens FEN generation)

Raylib is linked statically and configured in the Visual Studio project (`ChessProject.vcxproj`). The project targets **x64** Windows.

### 3.2 raygui

**raygui** is an immediate-mode GUI library built on top of Raylib. It is included via a single header (`raygui.h`) with `#define RAYGUI_IMPLEMENTATION` defined exactly once in `ChessProject.cpp`.

raygui provides:
- `GuiButton` — clickable buttons
- `GuiToggleGroup` — mutually exclusive radio-style toggle buttons (used for "VS Player / VS AI")
- `GuiCheckBox` — boolean toggles
- `GuiSliderBar` — continuous value sliders (audio volume, animation speed, Minimax depth)
- `GuiDropdownBox` — dropdown selectors (color picker target, engine selection)
- `GuiListView` — scrollable list (theme selection, model selection)
- `GuiColorPicker` — RGBA color picker for board square customization
- `GuiLoadStyle` — loads an `.rgs` style file to retheme the entire UI

GUI layouts for the menu and options screen are code-generated and stored in `Resources/GUI/MenuLayout.h` and `Resources/GUI/Options.h` respectively, each implementing an `InitGui*` and `GuiDrawGui*` function pattern.

### 3.3 subprocess.h

**subprocess.h** is a single-header C library by sheredom that manages child process creation and I/O pipe communication on Windows (and POSIX). It is used exclusively in `Stockfish.cpp` to:

- Spawn `stockfish.exe` as a child process (`subprocess_create`)
- Get stdin and stdout FILE* handles (`subprocess_stdin`, `subprocess_stdout`)
- Communicate over those handles with `fputs` / `fgets`
- Terminate the process on destruction (`subprocess_destroy`)

The library is included with `subprocess_option_enable_async` so that reading does not block the game thread indefinitely.

### 3.4 Stockfish Engine

**Stockfish** is an open-source, world-class chess engine. It is not compiled into this project — it runs as a **separate executable** (`stockfish/stockfish.exe` by default, configurable in Settings). Communication uses the **Universal Chess Interface (UCI)** protocol over stdin/stdout text lines.

The path to the Stockfish executable is stored in `Settings::StockfishPath` and can be changed through the Settings screen.

---

## 4. Architecture Overview

### 4.1 Class Hierarchy

```
Settings               (global static config, binary I/O)
│
├── Spot               (inherits Settings; one of 64 board cells)
│   └── ChessPiece*    (nullable pointer to the piece on this cell)
│
├── ChessPiece         (3D model, piece type, color, bounding box)
│
├── SelectedPiece      (tracks which piece is currently selected by the user)
│
├── IChessEngine       (pure virtual interface)
│   ├── MinimaxEngine  (custom alpha-beta engine, self-contained)
│   └── Stockfish      (subprocess wrapper, UCI protocol)
│
└── Board              (owns Spot[8][8], IChessEngine*, SelectedPiece)
    └── MoveAnimation  (struct: animated piece in flight)
```

`Board` is the central controller. It owns the 8×8 array of `Spot` objects, the currently selected piece state, and a pointer to whichever `IChessEngine` is active. It drives rendering, input processing, move execution, and synchronization between the visual board and the engine's internal state.

### 4.2 Game State Machine

The application runs a single `while (running)` loop. The current `GameState` enum value determines which case of a large `switch` statement executes each frame:

```
LoadingScreen  ──▶  MenuScreen  ──▶  GameScreen
                         │               │
                         ▼               ├──▶  PromotionScreen ──▶ GameScreen
                    SettingsScreen       │
                         │               ├──▶  PauseScreen ──▶ FileSelectionScreen
                         ▼                         │
                    (back to Menu)             GameScreen / MenuScreen
                                               │
                                           WinningScreen ──▶ LoadingScreen
```

`GameState` values:

| Value | Screen Shown |
|-------|-------------|
| `LoadingScreen` | Progress bar while board pieces are loaded one per frame |
| `MenuScreen` | Main menu: New Game, Settings, Exit, VS Player/AI toggle |
| `GameScreen` | Active 3D chess game |
| `SettingsScreen` | Full options panel |
| `PauseScreen` | In-game pause with Resume/Save/Load/Export/Menu buttons |
| `PromotionScreen` | Pawn promotion choice overlay |
| `WinningScreen` | Checkmate/Stalemate result overlay |
| `FileSelectionScreen` | File browser for save/load/export/model-swap |

---

## 5. Settings System (`Settings.h`)

`Settings` is a class whose **all data members are static**, making it a global singleton that any class in the project can access without holding a reference. Since `Spot` inherits from `Settings`, every spot on the board has access to board colors and model paths without indirection.

### 5.1 Static Members

| Member | Type | Description |
|--------|------|-------------|
| `Colors` | `vector<Color>` | 6 colors: selection, active, legal move, hover, light square, dark square |
| `ModelLocations` | `vector<string>` | 12 paths: LightKing, DarkKing, LightQueen, DarkQueen, LightBishop, DarkBishop, LightTower, DarkTower, LightKnight, DarkKnight, LightPawn, DarkPawn |
| `Styles` | `vector<string>` | Paths to `.rgs` raygui style files |
| `current_style` | `int` | Index into `Styles` |
| `StockfishPath` | `string` | Path to the Stockfish executable |
| `EngineType` | `int` | 0 = Stockfish, 1 = Minimax |
| `MinimaxDepth` | `int` | Search depth for Minimax (1–6, default 4) |
| `AnimationSpeed` | `float` | Multiplier applied to `GetFrameTime()` for move animation (default 3.0) |
| `AudioVolume` | `float` | 0–100 volume scale |
| `SoundEffects` | `bool` | Toggle sound effects |
| `AutoPromoteToQueen` | `bool` | Skip promotion UI and always promote to Queen |
| `EnableUndoRedo` | `bool` | Toggle undo/redo functionality |
| `ShowMoveHistory` | `bool` | Toggle the move history sidebar |
| `ShowEvalBar` | `bool` | Toggle the evaluation bar |
| `FiveQueensMode` | `bool` | ★ Toggle the Five Queens variant |

### 5.2 Binary Serialization

Settings are saved to `Settings.bin` using raw binary I/O (`ios::binary`). The serialization order is:

1. `numColors` (int) + each `Color` (4 bytes RGBA)
2. `numModels` (int) + each string as `(int size) + (chars)`
3. `numStyles` (int) + each string as `(int size) + (chars)`
4. `current_style` (int)
5. `StockfishPath` as `(int size) + (chars)`
6. `EngineType` (int), `MinimaxDepth` (int), `AnimationSpeed` (float)
7. `AudioVolume` (float), `SoundEffects` (bool), `AutoPromoteToQueen` (bool)
8. `EnableUndoRedo` (bool), `ShowMoveHistory` (bool), `ShowEvalBar` (bool)
9. `FiveQueensMode` (bool)

### 5.3 Forward Compatibility

The loading function reads fields sequentially and checks `MyFile.read(...)` return values. If a read fails (e.g., loading an older `Settings.bin` that does not contain newer fields), the missing fields are initialized to safe defaults. This allows the settings file to be upgraded across feature additions without corrupting existing user configurations.

---

## 6. Chess Piece Representation (`ChessPiece.cpp/.h`)

### 6.1 Piece Types

```cpp
enum Type { King, Queen, Bishop, Rook, Knight, Pawn };
```

Each `ChessPiece` holds:
- `Vector3 position` — 3D world-space position
- `bool colour` — `true` = white, `false` = black
- `Model model` — Raylib 3D model handle
- `BoundingBox box` — axis-aligned bounding box for collision detection
- `enum Type Name` — piece type

### 6.2 3D Model Loading

`CustomLoader()` maps the piece type and color to an index into `Settings::ModelLocations` and calls `LoadModel()`. The index mapping is:

| Index | Piece |
|-------|-------|
| 0 | Light (White) King |
| 1 | Dark (Black) King |
| 2 | Light Queen |
| 3 | Dark Queen |
| 4 | Light Bishop |
| 5 | Dark Bishop |
| 6 | Light Rook (Tower) |
| 7 | Dark Rook (Tower) |
| 8 | Light Knight |
| 9 | Dark Knight |
| 10 | Light Pawn |
| 11 | Dark Pawn |

Models are `.glb` (GL Transmission Format binary) files loaded at runtime. The `Resources/ChessSet/` folder is gitignored — users must supply their own `.glb` models.

The destructor calls `UnloadModel(model)` to free GPU resources.

### 6.3 Bounding Box System

`UpdateBoundingBox()` computes the world-space bounding box by adding the piece's `position` offset to the model's local bounding box extents. This bounding box is used by `GetRayCollisionBox` for mouse picking (though the actual picking is done against the board squares, not individual pieces).

---

## 7. Board Spot System (`Spot.cpp/.h`)

`Spot` represents one of the 64 squares on the chessboard. It inherits from `Settings` to access board colors.

**Members:**
- `Vector3 position` — the 3D center of the square
- `ChessPiece* piece` — pointer to the occupying piece, or `nullptr`
- `bool colour` — `true` = light square, `false` = dark square
- `BoundingBox spotbox` — a 1×1×1 cube centered on `position`, used for raycasting

**`Draw()`** renders the board square as a colored cube:
```cpp
DrawCube(position, 1.0f, 1.0f, 1.0f, colour ? Colors[4] : Colors[5]);
```
`Colors[4]` is the light square color (default: `{189,125,85,255}`) and `Colors[5]` is the dark square color (default: `{83,57,48,255}`).

**`DrawPiece()`** delegates to `piece->Draw()`, which calls Raylib's `DrawModel`.

The board array `Board::board[8][8]` maps `board[row][col]` where:
- `row` 0 = rank 1 (white's back rank)
- `row` 7 = rank 8 (black's back rank)
- `col` 0 = file a, `col` 7 = file h

---

## 8. Piece Selection System (`SelectedPiece.cpp/.h`)

`SelectedPiece` tracks the single piece that a player has currently selected, and provides the visual highlight cube for it.

**Members:**
- `int row, col` — board coordinates of the selected piece
- `bool selected` — selection state flag
- `Spot* current` — pointer to the selected spot

**Key methods:**

- `SetSelectedPiece(i, j, spot)` — records selection state; called when the user left-clicks a piece
- `IsSelected()` — returns `selected`
- `Validate(i, j)` — returns `true` if `(i,j)` is the currently selected square (used to prevent re-selecting the same square as the move target)
- `ToggleSelected()` — flips `selected`; called after a move is committed
- `Working()` — called every frame while a piece is selected; draws a colored cube over the selected square using `Settings::Colors[1]` (green by default)
- `Unselect()` — forcibly sets `selected = false`

---

## 9. Board Logic (`Board.cpp/.h`)

`Board` is the heart of the game. It manages the visual board, drives input handling, executes moves through the engine, and synchronizes the 3D scene with the engine's internal state.

### 9.1 Board Initialization — Async Loading

The constructor `Board()` only sets initial state flags (no pieces are created). Piece loading happens incrementally in `Board::Init(float& progress)`.

`Init()` is a **coroutine-style incremental loader**. It uses `static` variables `i`, `j`, and `color` to remember progress between calls. Each call processes **one cell** of the 8×8 board, creates a `ChessPiece` for it if needed, and returns `true`. When all 64 cells are processed, it returns `false`.

The loading screen in `ChessProject.cpp` calls `Init()` in a tight loop, rendering one frame of the progress bar for each batch of cells, allowing the OS to refresh the window during what would otherwise be a blocking load. Progress is tracked as a percentage (each cell advances it by `1.5625`, since `64 × 1.5625 = 100`).

The standard starting position layout is:

| Row (board index) | Contents |
|-------------------|----------|
| 0 | White: R, N, B, Q, K, B, N, R |
| 1 | White pawns |
| 2–5 | Empty |
| 6 | Black pawns |
| 7 | Black: R, N, B, Q, K, B, N, R |

### 9.2 DrawBoard — Render Loop

Called once per game frame inside `BeginMode3D`. It:

1. If `anim.active`, advances the animation and checks for completion (see §9.3).
2. Iterates all 64 squares, calling `board[i][j].Draw()` and `board[i][j].DrawPiece()` (if occupied).
3. If `anim.active` and `anim.piece != nullptr`, draws the animating piece on top of everything else (so it floats above the board during its transit).

### 9.3 Move Animation System

The `MoveAnimation` struct tracks an in-progress piece movement:

```cpp
struct MoveAnimation {
    bool active;
    ChessPiece* piece;      // the piece being animated
    Vector3 startPos;       // world position at start
    Vector3 endPos;         // world position at destination
    float progress;         // 0.0 → 1.0
    int startRow, startCol, endRow, endCol;
    bool isWhiteTurnNext;   // whose turn it is after animation completes
};
```

**How it works:**

- When `StartAnimation(move, nextTurnWhite)` is called, the piece pointer is detached from `board[startRow][startCol].piece` (set to `nullptr`) and stored in `anim.piece`. This prevents double-drawing.
- Each frame, `progress += dt * Settings::AnimationSpeed`. The piece's 3D position is interpolated using `Vector3Lerp(startPos, endPos, progress)`.
- Frame time is clamped to `0.1f` to prevent huge position jumps when the AI thinking blocks the frame.
- When `progress >= 1.0f`, the animation completes: the captured piece (if any) at the destination is deleted, the animated piece is placed into `board[endRow][endCol].piece`, `UpdateChessboard()` is called to sync the visual board with the engine, `whiteTurn` is set, and win status is checked.

While an animation is active, all input methods (`Selecter`, `MakeMove`, `AIMove`) return immediately, preventing the player from making moves mid-animation.

### 9.4 Selecter — Raycasting Input

`Board::Selecter(Ray SelectRay, RayCollision check)` handles piece selection via 3D raycasting:

1. A `Ray` is cast from the camera through the mouse position using Raylib's `GetMouseRay`.
2. The method iterates all 64 `Spot` bounding boxes and tests `GetRayCollisionBox(SelectRay, board[i][j].spotbox)` for each.
3. To avoid selecting a square behind a closer one, it tracks the **closest hit** by comparing `col.distance`.
4. If no piece is selected and the hit square has a piece, a hover highlight is drawn and left-click sets the selection.
5. If a piece is already selected and the user clicks the same square again, the selection is toggled off.

The cursor is hidden when right-click is held (free camera mode), and `Selecter` guards against this with `!IsCursorHidden()`.

### 9.5 Legal Move Highlighting

`DrawLegalMoves()` is called every frame while a piece is selected:

1. It constructs an algebraic position string from the selected piece's column and row (e.g., `"e2"`).
2. It queries `engine->list_legal_moves(position)` to get all legal moves from that square (e.g., `["e2e3", "e2e4"]`).
3. The destination part of each move string (characters 2–3) is decoded to board indices.
4. A blue cube (`Colors[2]`) is drawn over each legal destination square.
5. The list of legal move strings is returned to the game loop for use in `MakeMove`.

### 9.6 MakeMove and DoMove

`MakeMove(SelectRay, checker, moves)` listens for clicks on highlighted legal move squares:

1. Raycasts to find the hovered square (same closest-hit logic as `Selecter`).
2. Checks if the hovered square is in the `moves` list.
3. If it is, draws an orange highlight (`Colors[3]`) and on left-click calls `DoMove(row, col)`.

`DoMove(row, col)` is the core move commitment function:

1. Constructs a UCI move string from the selected piece's position and the target: `"e2e4"`.
2. **Pawn promotion check:** if the piece is a pawn reaching rank 1 or rank 8, and `AutoPromoteToQueen` is off, it sets `isPromotionPending = true`, stores the partial move in `pendingPromotionMove`, and returns — switching the state to `PromotionScreen` next frame.
3. If not promoting (or auto-promoting), it appends `'q'` automatically.
4. The move is appended to `fullMoveHistory` at `currentMoveIndex` (truncating any future moves if undos had been performed).
5. `engine->update_moves(line)` notifies the engine of the move.
6. `StartAnimation(line, false)` kicks off the visual animation.

### 9.7 UpdateChessboard — FEN Sync

`UpdateChessboard()` is the synchronization bridge between the engine's internal state and the Raylib 3D board. It is called after every animation completes.

It calls `engine->BoardMaker()` which returns an `8x8` vector of chars (uppercase = white, lowercase = black, `'E'` = empty). The FEN row-0 from `BoardMaker` corresponds to rank 8 (top of board), which maps to `board[7]` in the visual array (because the visual board uses `board[0]` = rank 1).

For each cell, it compares the expected piece type and color against what is currently on the visual board. If there's a mismatch (type changed due to promotion, piece added due to engine-side computation, piece removed due to capture), it deletes the old `ChessPiece` and creates a new one of the correct type and color at the correct 3D position.

### 9.8 Pawn Promotion

Promotion is handled in two stages:

1. **Detection in `DoMove`:** When a pawn reaches the promotion rank, if `AutoPromoteToQueen` is `false`, the game state transitions to `PromotionScreen`.
2. **Completion in `CompletePromotion(char pieceChar)`:** Called from the `PromotionScreen` UI with one of `'q'`, `'r'`, `'b'`, `'n'`. The character is appended to `pendingPromotionMove`, making it a 5-character UCI string (e.g., `"e7e8q"`). The move is then committed to history and animation is started.

### 9.9 Undo/Redo System

The undo/redo system uses a **move history list with a cursor pointer**:

- `fullMoveHistory` (vector of UCI move strings) stores every committed move.
- `currentMoveIndex` points to how many of those moves are currently applied.
- **Undo:** decrements `currentMoveIndex`, then calls `ApplyMovesToCurrentIndex()`.
- **Redo:** increments `currentMoveIndex`, then calls `ApplyMovesToCurrentIndex()`.
- Any new move made after an undo **truncates** `fullMoveHistory` from `currentMoveIndex` onward, preventing branching timelines.

`ApplyMovesToCurrentIndex()`:
1. Calls `engine->set_moves(movesToApply)` with a slice of the history up to `currentMoveIndex`. Both engines re-replay the entire move list from the start position.
2. Calls `UpdateChessboard()` to resync visuals.
3. Recalculates whose turn it is: white moves if `currentMoveIndex % 2 == 0`.
4. Re-runs `WinChecker`.

Input bindings: **Left Arrow** or **Ctrl+Z** for undo, **Right Arrow** or **Ctrl+Y** for redo.

### 9.10 Save, Load, and PGN Export

**`SaveGame(filename)`** writes all moves in `fullMoveHistory` as space-separated UCI strings to a plain-text file.

**`LoadGame(filename)`** reads the file back, repopulates `fullMoveHistory`, sets `currentMoveIndex = fullMoveHistory.size()`, and calls `ApplyMovesToCurrentIndex()`.

**`ExportPGN(filename)`** writes a minimal Portable Game Notation file with standard headers and the move list. Moves are currently output as raw UCI strings (e.g., `e2e4`) rather than fully annotated SAN (e.g., `e4`). The `UciToSan()` method is a placeholder that returns the input unchanged — full SAN conversion is not yet implemented.

### 9.11 Win Detection

`Board::winStatus` holds:
- `0` — game in progress
- `1` — white wins (black checkmated)
- `2` — black wins (white checkmated)
- `3` — stalemate

It is set by `engine->WinChecker(board)` after each move animation completes. The game loop transitions to `WinningScreen` when `winStatus != 0` and no animation is active.

---

## 10. AI Engine Interface (`IChessEngine.h`)

`IChessEngine` is a **pure abstract base class** that defines the contract all chess engine backends must fulfill:

```cpp
class IChessEngine {
public:
    virtual ~IChessEngine() = default;
    virtual vector<string> list_all_legal_moves() = 0;
    virtual vector<string> list_legal_moves(string position) = 0;
    virtual void update_moves(string move) = 0;
    virtual string FenExtracter() = 0;
    virtual vector<vector<char>> BoardMaker() = 0;
    virtual int WinChecker(Spot board[8][8]) = 0;
    virtual string GetBestMove(int depth) = 0;
    virtual void set_moves(const vector<string>& current_moves) = 0;
    virtual float GetEvaluation() = 0;
    virtual void set_starting_fen(const string& fen) = 0;
};
```

**Method responsibilities:**

| Method | Purpose |
|--------|---------|
| `list_all_legal_moves()` | Return all legal moves in current position as UCI strings |
| `list_legal_moves(pos)` | Return legal moves from a specific square (e.g., `"e2"`) |
| `update_moves(move)` | Apply a single move to the engine's internal state |
| `FenExtracter()` | Return the current position as a FEN string |
| `BoardMaker()` | Return the board as an 8×8 char grid for visual sync |
| `WinChecker(board)` | Detect checkmate/stalemate; return 0/1/2/3 |
| `GetBestMove(depth)` | Run search and return the best move UCI string |
| `set_moves(moves)` | Reset and replay a full list of moves (for undo/redo) |
| `GetEvaluation()` | Return current position evaluation in pawn units |
| `set_starting_fen(fen)` | Set a non-standard starting position (Five Queens Mode) |

`Board::engine` is a raw `IChessEngine*`. The engine is created in `Board::InitEngine()` based on `Settings::EngineType`:

```cpp
if (Settings::EngineType == 0)
    engine = new Stockfish();
else
    engine = new MinimaxEngine();
```

---

## 11. Minimax Engine (`MinimaxEngine.cpp/.h`)

The `MinimaxEngine` is a fully self-contained chess AI written in C++ with no external process. It implements the `IChessEngine` interface and is the only engine that fully supports the Five Queens Mode via FEN loading.

### 11.1 Internal Board Representation

The engine uses an `int board[8][8]` where:

| Value | Piece |
|-------|-------|
| `0` | Empty |
| `1` | White Pawn |
| `2` | White Knight |
| `3` | White Bishop |
| `4` | White Rook |
| `5` | White Queen |
| `6` | White King |
| `-1` | Black Pawn |
| `-2` | Black Knight |
| `-3` | Black Bishop |
| `-4` | Black Rook |
| `-5` | Black Queen |
| `-6` | Black King |

Positive values are white, negative values are black. This sign convention allows `isWhitePiece(p) = p > 0` and `abs(p)` to get the piece type regardless of color.

Additional state:
- `bool whiteToMove` — whose turn it is
- `bool castlingRights[4]` — indexed as `[K, Q, k, q]`
- `int enPassantCol` — column of the pawn that just double-pushed, or `-1`
- `int enPassantRow` — row of the en passant capture target
- `vector<string> moveHistory` — for replay
- `string starting_fen` — non-standard start position (Five Queens)

### 11.2 Move Representation

Moves are UCI strings: `"e2e4"` (4 chars) or `"e7e8q"` (5 chars with promotion). Helper methods convert between algebraic and (row, col) indices:

```cpp
string squareToAlgebraic(int row, int col);  // e.g., row=1, col=4 → "e2"
void algebraicToSquare(const string& s, int& row, int& col);
```

### 11.3 Pseudo-Legal Move Generation

`generateAllPseudoLegalMoves(bool forWhite)` generates all moves that are structurally valid for the moving side but **does not check whether they leave the king in check**. This is the first pass.

**Per piece type:**

**Pawn:**
- Single push forward (if square is empty)
- Double push from starting rank (both squares empty)
- Diagonal captures (opponent piece on diagonal)
- Promotion suffix `'q'` appended when reaching the promotion rank
- En passant: if the target square matches `enPassantCol` and `enPassantRow`

**Knight:** All 8 L-shaped offsets `{±1,±2}` and `{±2,±1}`, bounded to the board.

**Bishop, Rook, Queen:** Ray-casting along direction sets:
- Bishop: 4 diagonal directions
- Rook: 4 straight directions
- Queen: all 8 directions (full union of bishop and rook)

Each ray extends until hitting the board edge, a friendly piece (stop before), or an enemy piece (include that square then stop).

**King:** All 8 adjacent squares. Additionally:

- **Kingside castling:** checks `castlingRights[0/2]`, that intermediate squares are empty, and that the king does not pass through or end on an attacked square.
- **Queenside castling:** same but for files b, c, d.

### 11.4 Legal Move Filtering

`generateAllLegalMoves(bool forWhite)` calls `generateAllPseudoLegalMoves`, then for each candidate:

1. Applies the move with `applyMove(mv, undo)`.
2. Checks `isInCheck(forWhite)` — if the moving side's king is still in check, the move is illegal.
3. Undoes the move with `undoMove(undo)`.
4. Only appends the move to `legal` if the king is not in check after it.

### 11.5 Apply and Undo Move (MoveUndo)

`MoveUndo` is a struct that captures all state needed to fully reverse a move:

```cpp
struct MoveUndo {
    int fromRow, fromCol, toRow, toCol;
    int movedPiece;
    int capturedPiece;
    bool castlingRights[4];
    int enPassantCol;
    bool wasEnPassant;
    bool wasCastling;
    int promotedTo;
};
```

`applyMove(move, undo)`:
1. Fills the `undo` struct with current state.
2. Handles en passant: removes the captured pawn from the board (it's on a different row than the destination).
3. Updates en passant state for double pawn pushes.
4. Handles castling: moves the rook to its post-castling square.
5. Moves the piece, applies promotion if the move string is 5 chars long.
6. Updates castling rights if kings or rooks moved.
7. Flips `whiteToMove`.

`undoMove(undo)`:
1. Flips `whiteToMove` back.
2. Restores `castlingRights` and `enPassantCol/Row`.
3. Restores `board[fromRow][fromCol]` to `movedPiece` (or the pre-promotion pawn).
4. Restores `board[toRow][toCol]` to `capturedPiece` (empty square for non-captures).
5. If en passant, restores the captured pawn to its original square.
6. If castling, moves the rook back.

### 11.6 Static Evaluation Function

`evaluate()` returns a score in centipawns from white's perspective (positive = white advantage):

```
score = Σ (pieceValue + positionalBonus) for white pieces
      - Σ (pieceValue + positionalBonus) for black pieces
```

**Piece values:**

| Piece | Value (centipawns) |
|-------|-------------------|
| Pawn | 100 |
| Knight | 320 |
| Bishop | 330 |
| Rook | 500 |
| Queen | 900 |
| King | 20000 |

### 11.7 Piece-Square Tables

Each piece type has an 8×8 bonus table that incentivizes good positional play. Tables are defined from white's perspective (row 0 = rank 1). For black pieces, the row index is mirrored: `r = 7 - row`.

**Design rationale per table:**

- **Pawn table:** High bonuses in the center (d4/e4/d5/e5) and extreme bonuses on the 7th rank (promotion proximity). Penalties for doubled/backward pawns are approximated by the positional penalties on edge files in the early ranks.
- **Knight table:** Large penalties on the edges and corners (`-50` in corners), bonuses toward the center (up to `+20` at d4/e4/d5/e5). Knights are notoriously weak on the board edge.
- **Bishop table:** Moderate center bonuses, significant penalties on corners. Rewards long diagonals.
- **Rook table:** Bonus on the 7th rank (`+5`), bonus for the d/e files on rank 1, otherwise relatively flat. Encourages open file occupation.
- **Queen table:** Slight center bonuses, penalties on corners. Discourages early queen development (which can lose tempo).
- **King table:** Large penalties everywhere except the corners (`+20/30` behind a pawn shield on ranks 1-2). Strongly encourages king safety and castling.

### 11.8 Minimax with Alpha-Beta Pruning

`minimax(int depth, int alpha, int beta, bool maximizing)`:

**Base case:** at `depth == 0`, returns `evaluate()` (leaf node static evaluation).

**Terminal nodes:**
- If no legal moves exist and king is in check: **checkmate**. Returns `±KING_VALUE` adjusted by `depth` to prefer faster mates.
- If no legal moves but no check: **stalemate**. Returns `0`.

**Recursive case:**

```
Maximizing (white):
    bestScore = -∞
    for each legal move:
        apply move
        score = minimax(depth-1, alpha, beta, false)
        undo move
        bestScore = max(bestScore, score)
        alpha = max(alpha, score)
        if beta ≤ alpha: break  // Beta cutoff (opponent won't allow this)
    return bestScore

Minimizing (black):
    bestScore = +∞
    for each legal move:
        apply move
        score = minimax(depth-1, alpha, beta, true)
        undo move
        bestScore = min(bestScore, score)
        beta = min(beta, score)
        if beta ≤ alpha: break  // Alpha cutoff (we already have a better option)
    return bestScore
```

**Alpha-beta pruning** drastically reduces the number of nodes evaluated. In the best case (perfect move ordering), it reduces the effective branching factor from `b` to `√b`, effectively doubling the reachable depth for the same computation. In practice, the move ordering heuristic (see §11.9) provides significant real-world improvement.

### 11.9 Move Ordering Optimization

Before the minimax loop, moves are sorted with a comparator that places **captures first** and orders captures by the **value of the captured piece** (highest value first):

```cpp
sort(moves.begin(), moves.end(), [&](const string& a, const string& b) {
    int va = abs(board[destRow_a][destCol_a]);  // piece value at destination
    int vb = abs(board[destRow_b][destCol_b]);
    return va > vb;  // larger capture value first
});
```

Captures tend to create large score swings and are more likely to cause cutoffs early in the search, making this heuristic highly effective in practice.

### 11.10 Win/Stalemate Detection

`WinChecker(Spot sboard[8][8])` (the `Spot` board parameter is unused — it queries the internal int board):

1. Generates all legal moves for `whiteToMove`.
2. If moves exist: return `0` (game continues).
3. If no moves and in check: return `2` if white is to move (white lost), `1` if black is to move (black lost).
4. If no moves and not in check: return `3` (stalemate).

### 11.11 FEN Loading and Extraction

**`loadFEN(fen)`** parses a standard FEN string and repopulates the internal board:
- Iterates the piece placement section, mapping chars to `charToPiece()` values.
- Sets `whiteToMove` from the active color field.
- Parses castling rights from the castling field.
- Parses en passant from the en passant field.

**`FenExtracter()`** generates a FEN string from the current internal state:
- Encodes piece placement by scanning rows 7→0 (rank 8→1).
- Appends active color, castling rights, en passant target, then `" 0 1"` for halfmove and fullmove clocks.

**`set_starting_fen(fen)`** stores the FEN and calls `loadFEN`. Used to initialize Five Queens Mode.

**`set_moves(moves)`** re-loads `starting_fen` (or standard position if empty) and replays the entire move list — used by the undo/redo system.

---

## 12. Stockfish Engine Integration (`Stockfish.cpp/.h`)

### 12.1 Process Management via subprocess.h

The `Stockfish` constructor:

```cpp
command[0] = Settings::StockfishPath.c_str();
subprocess_create(command, subprocess_option_enable_async, &stockfish);
stock_in = subprocess_stdin(&stockfish);
stock_out = subprocess_stdout(&stockfish);
```

This creates the Stockfish child process and gives direct access to its stdin/stdout as FILE* handles. The async flag prevents blocking reads from hanging the game thread indefinitely.

### 12.2 UCI Communication Protocol

All communication uses line-terminated text commands:

- `input_stockfish(query)` — writes a string to Stockfish's stdin with `fputs` + `fflush`
- `read_stockfish()` — reads one line from Stockfish's stdout with `fgets`

**Key UCI commands used:**

| Command | Purpose |
|---------|---------|
| `position startpos moves e2e4 ...` | Set position by replaying moves from start |
| `position fen <FEN> moves ...` | Set position from a FEN string |
| `go perft 1` | Generate all legal moves (perft depth 1) |
| `go depth N` | Search to depth N and return best move |
| `go movetime 1` | Search for 1ms (fast win detection) |
| `d` | Display board state, FEN, and checker information |

### 12.3 Legal Move Query via Perft

`list_all_legal_moves()` sends `"go perft 1\n"` and reads lines until it sees `"Nodes"`. Each intermediate line has the format `"e2e4: 1"` — the move string before `": "` is extracted:

```cpp
if (out.find(": ") != string::npos) {
    legalmoves.push_back(out.substr(0, colonPos));
}
```

`list_legal_moves(position)` filters the full list to moves starting with the given square string.

### 12.4 Board State Extraction

`FenExtracter()` sends `"d\n"` and reads until a line starting with `"Fen: "`, then returns the rest of that line as the FEN.

`BoardMaker()` calls `FenExtracter()` to get the FEN, then parses the piece placement section into an 8×8 `vector<vector<char>>` grid. The parsing logic mirrors the FEN row/column convention (`/` = next row, digit = skip N columns).

### 12.5 Win Detection via Stockfish

`WinChecker(Spot board[8][8])`:

1. Sends `"go movetime 1\n"` and reads until `"bestmove "`.
2. If `bestmove` response is `"(none)"`, there are no legal moves:
   - Sends `"d\n"` and reads until `"Checkers: "`.
   - If the checkers line is empty (`"\r\n"`): **stalemate** → return `3`.
   - Otherwise, reads the first checker square and looks up the piece color on the visual board to determine who is in check → return `1` (white wins) or `2` (black wins).
3. If `bestmove` is not `"(none)"`: game continues → return `0`.

### 12.6 Best Move and Evaluation

`GetBestMove(int depth)` sends `"go depth N\n"` and reads until `"bestmove "`, then extracts the move before any space or newline.

`GetEvaluation()` sends `"go depth 1\n"` and parses `"score cp"` (centipawns) or `"score mate"` from the info lines. Mate scores are mapped to `±100.0f`. The score is negated if it's black's turn (since Stockfish always reports from the side to move's perspective, but the HUD shows white's advantage).

### 12.7 Starting FEN Support

`set_starting_fen(fen)` sends `"position fen <fen>\r\n"` to Stockfish. `update_moves` and `set_moves` then append moves to this FEN base rather than `startpos`. This is the mechanism that enables Five Queens Mode with the Stockfish backend.

---

## 13. Five Queens Mode — Complete Implementation

Five Queens Mode is the distinctive feature added for the AI lab project. It modifies the standard chess starting position to include five queens in total (two per side plus one neutral extra), creating a materially richer position that exercises the AI's evaluation and pruning code more aggressively.

### 13.1 Concept and Design Goals

In standard chess, each side begins with exactly one queen. This mode:

1. Gives **white two queens** — the standard queen on d1, plus an additional queen placed randomly on white's home ranks (ranks 1–2, excluding d1 and e1).
2. Gives **black two queens** — the standard queen on d8, plus an additional queen placed randomly on black's home ranks (ranks 7–8, excluding d8 and e8).
3. Adds a **fifth "wild" queen** — randomly assigned to either white or black, placed on a randomly chosen empty square in the middle four ranks (ranks 3–6).

The result is a position with unprecedented queen activity, ensuring that AI search trees are populated with high-value captures early in the game, which both stresses alpha-beta pruning effectiveness and demonstrates the AI's ability to reason about multi-queen interactions.

### 13.2 FEN Generation Algorithm (`GenerateFiveQueensFen`)

`Board::GenerateFiveQueensFen()` is a `static` method that generates a valid FEN string for a randomized Five Queens position. Here is a step-by-step breakdown:

**Step 1 — Initialize with the standard starting layout:**

```cpp
char boardArray[8][8] = {
    {'r','n','b','q','k','b','n','r'},  // rank 8 (black back rank)
    {'p','p','p','p','p','p','p','p'},  // rank 7
    {' ',' ',' ',' ',' ',' ',' ',' '},  // ranks 3-6 (empty)
    ...
    {'P','P','P','P','P','P','P','P'},  // rank 2
    {'R','N','B','Q','K','B','N','R'}   // rank 1 (white back rank)
};
```

**Step 2 — Place the extra white queen:**

Eligible squares are all cells in rows 6–7 of the array (ranks 1–2 in chess), excluding row 7 columns 3 and 4 (which are `'Q'` the original queen and `'K'` the king at d1/e1). A random index is chosen from this eligible set using `GetRandomValue`, and a `'Q'` is placed there, potentially **replacing** the piece that was occupying that square (e.g., replacing a pawn or a rook).

**Step 3 — Place the extra black queen:**

Eligible squares are rows 0–1 (ranks 7–8), excluding row 0 columns 3 and 4 (d8/e8). The same random selection process places a `'q'` there.

**Step 4 — Place the fifth wild queen:**

Eligible squares are all cells in rows 2–5 (ranks 3–6), which start empty. A random index is chosen. The queen's color is determined by `GetRandomValue(0, 1)`: `0` → `'Q'` (white), `1` → `'q'` (black).

**Step 5 — Encode as FEN:**

The `boardArray` is traversed row by row (row 0 = rank 8, row 7 = rank 1 to match FEN convention). Empty cells (` `) are counted and emitted as digits; non-empty cells are emitted as their character. Rows are separated by `/`. The position suffix `" w KQkq - 0 1"` is appended, indicating white to move, full castling rights, no en passant.

**Example output FEN:**

```
rnbqkbnr/ppQppppp/8/4q3/8/8/PPPPPPqP/RNBQKBNR w KQkq - 0 1
```

This encodes a position where black has an extra queen on c7 (replacing a pawn), white has an extra queen somewhere, and the wild queen is in the center.

### 13.3 Integration with the Game Loop

In `ChessProject.cpp`, when the game transitions from `MenuScreen` to `GameScreen`:

```cpp
chessboard->InitEngine();
chessboard->isAIMode = (menustate.ToggleGroup004Active == 1);
if (Settings::FiveQueensMode) {
    string fen = Board::GenerateFiveQueensFen();
    chessboard->engine->set_starting_fen(fen);
    chessboard->ApplyMovesToCurrentIndex();
}
```

`set_starting_fen(fen)` passes the generated FEN to the active engine:
- **Minimax:** calls `loadFEN(fen)` to parse the position directly into its `int board[8][8]`.
- **Stockfish:** sends `"position fen <fen>\r\n"` over the subprocess pipe.

`ApplyMovesToCurrentIndex()` then calls `UpdateChessboard()` to sync the Raylib 3D board with the new starting position, making the extra queens appear as 3D models on the board immediately.

### 13.4 Compatibility with Both Engines

Both AI engines support Five Queens Mode without modification to their core logic:

- **MinimaxEngine** is fully FEN-aware. `loadFEN` correctly populates multiple queens per side. The evaluation function naturally handles the extra queens (they contribute `900` centipawns each to the material score). The move generator handles any number of queens per side since it iterates all squares.

- **Stockfish** natively supports arbitrary FEN positions including those with multiple queens. Setting the starting position via `"position fen ..."` is a standard UCI feature. All legal move generation, evaluation, and best move search work correctly.

### 13.5 Implications for Gameplay

- **Material asymmetry:** The wild fifth queen may belong to either side, creating an inherently unbalanced position. This tests whether the AI can accurately evaluate and exploit material advantage.
- **Early queen exposure:** Extra queens placed on home ranks or center squares are immediately active, leading to earlier tactical complications.
- **Pawn structure disruption:** The extra queen placement may replace a pawn or piece on the home ranks, weakening one side's pawn structure from move one.
- **N-Queens relevance:** With up to 3 queens of the same color on the board, the position naturally demonstrates N-Queens-style conflict (queens attacking each other's lines), linking directly to the N-Queens problem that motivates the lab project.

---

## 14. Main Entry Point (`ChessProject.cpp`)

### 14.1 Window and Camera Initialization

```cpp
const int ScreenWidth = 1920;
const int ScreenHeight = 1080;
```

The window is opened at 1920×1080 but marked resizable with `SetWindowState(FLAG_WINDOW_RESIZABLE)`. The ESC key is disabled as a window-close key (`SetExitKey(0)`) so it can be used for in-game pause. Target FPS is 60.

The 3D camera is initialized as a perspective camera:
```cpp
camera.position = { 0.1f, 5.0f, 0.1f };
camera.target   = { 1.0f, 3.5f, 1.0f };
camera.up       = { 0.0f, 1.0f, 0.0f };
camera.fovy     = 90.0f;
camera.projection = CAMERA_PERSPECTIVE;
```

Static members of `Settings` are explicitly initialized at the top of `main()` since they are `static` class members requiring a definition point in one translation unit.

### 14.2 Game State Loop

```cpp
while (running) {
    switch (State) {
        case LoadingScreen: ...
        case MenuScreen:    ...
        case GameScreen:    ...
        // etc.
    }
}
CloseWindow();
```

Each case handles its own `BeginDrawing()`/`EndDrawing()` pair.

### 14.3 Loading Screen State

Calls `chessboard->Init(loadingProgress)` in a tight inner loop until it returns `false` (all cells loaded), drawing a progress bar each frame. Transitions to `NextStateAfterLoading` (either `MenuScreen` or `GameScreen`, depending on context — reusing the loading screen for new game resets).

### 14.4 Menu Screen State

Renders using `GuiMenuLayout(&menustate, State)`. The menu layout has a game mode toggle (`ToggleGroup004`) with values `"VS Player"` (0) and `"VS AI"` (1). On transition to `GameScreen`, this sets `chessboard->isAIMode`.

### 14.5 Game Screen State

The most complex state. Per frame:

1. Handles window close and ESC→Pause.
2. Checks undo/redo keys.
3. `BeginDrawing()` → `ClearBackground(LIGHTGRAY)` → `BeginMode3D(camera)`.
4. If right mouse is pressed, toggles cursor hide/show for free camera mode.
5. If cursor is hidden, calls `UpdateCamera(&camera, CAMERA_FREE)` for Raylib's built-in free-look camera.
6. `chessboard->DrawBoard()` — renders the 3D scene.
7. Raycasting: `GetMouseRay` → `Selecter` → `currentpiece.Working()` → if selected: `DrawLegalMoves` + `MakeMove`.
8. If `isPromotionPending`, transitions to `PromotionScreen`.
9. `AIMove()` — if AI mode and it's black's turn, triggers the AI move.
10. `DrawGrid(20, 1.0f)` — draws the reference grid.
11. `EndMode3D()`.
12. Renders 2D overlays: evaluation bar, move history panel, FPS counter.
13. Checks `winStatus` and transitions to `WinningScreen` if nonzero.

### 14.6 Pause Screen State

Renders buttons for Resume, Save Game, Load Game, Export PGN, and Main Menu. Save/Load/Export buttons set `fileActionTarget` (1, 2, 3 respectively) and transition to `FileSelectionScreen`.

### 14.7 Promotion Screen State

Renders the 3D board in the background with a dark overlay, then shows four `GuiButton` widgets for Queen, Rook, Bishop, Knight. Clicking one calls `chessboard->CompletePromotion(pieceChar)` and returns to `GameScreen`.

### 14.8 Winning Screen State

Displays `"White Won!"`, `"Black Won!"`, or `"Stalemate!"`. Provides `"New Game"` (reloads from `LoadingScreen` targeting `GameScreen`) and `"Main Menu"` buttons.

### 14.9 File Selection Screen State

Renders `GuiWindowFileDialog`. When the dialog is closed (selection made), `fileActionTarget` determines the action:
- `0` — model file replacement (settings context)
- `1` — `SaveGame(selectedPath)`
- `2` — `LoadGame(selectedPath)`
- `3` — `ExportPGN(selectedPath)`

### 14.10 Settings Screen State

Delegates entirely to `GuiOptions(&optionstate, options, State)` from `Resources/GUI/Options.h`.

### 14.11 Evaluation Bar and Move History HUD

**Evaluation Bar** (when `Settings::ShowEvalBar`):
- Gets `eval = engine->GetEvaluation()` (pawns, white-positive).
- Clamps to `[-10, 10]`.
- Maps to a `0–1` white percentage: `whitePercent = (eval + 10) / 20`.
- Draws a vertical bar at `x=20`, `height = ScreenHeight - 100`: top portion is dark grey (black's share), bottom is white.
- Draws the numeric eval to the right of the bar.

**Move History Panel** (when `Settings::ShowMoveHistory`):
- A 200×(ScreenHeight-100) panel at the right edge.
- Iterates `fullMoveHistory[0..currentMoveIndex]`, formatting moves in pairs: move number, white's move (left column), black's move (right column).
- Automatically scrolls to show the most recent moves when the list exceeds the panel height.

---

## 15. Frontend and GUI System

### 15.1 raygui Immediate-Mode GUI

raygui uses an immediate-mode paradigm: **there are no persistent widget objects**. Each frame, the draw function is called with the current state struct as argument, and all widgets are both drawn and polled for interaction in a single call. Widget return values or state struct fields indicate user interaction.

### 15.2 MenuLayout.h — Main Menu

`GuiMenuLayoutState` holds:
- `bool WindowBox000Active` — whether the main window is open (used as a quit signal)
- `int ToggleGroup004Active` — 0 = VS Player, 1 = VS AI
- `Rectangle layoutRecs[6]` — pre-computed widget positions

`InitGuiMenuLayout()` computes anchored positions relative to `MainAnchor`. The layout includes:
- A `WindowBox` that serves as the overall container (closing it sets `WindowBox000Active = false`, which the main loop interprets as a quit request)
- A `Label` for the game title
- Three buttons: Play Game, Settings, Exit Game
- A `ToggleGroup` for VS Player / VS AI mode selection

`GuiMenuLayout(&state, State)` takes the game state by reference so it can directly set `State = GameScreen` or `State = SettingsScreen` from within the layout function.

### 15.3 Options.h — Settings Screen

`GuiOptionsState` holds all options panel widget state:

| Field | Widget | Purpose |
|-------|--------|---------|
| `AudioSliderBarValue` | SliderBar | Master volume |
| `SoundEffectCheckBoxChecked` | CheckBox | Toggle sound effects |
| `AutoQueenCheckBoxChecked` | CheckBox | Auto-promote to queen |
| `EnableUndoRedoCheckBoxChecked` | CheckBox | Undo/Redo toggle |
| `ShowMoveHistoryCheckBoxChecked` | CheckBox | Move history panel |
| `ShowEvalBarCheckBoxChecked` | CheckBox | Evaluation bar |
| `FiveQueensModeCheckBoxChecked` | CheckBox | ★ Five Queens Mode |
| `ListViewThemesActive` | ListView | Selected theme index |
| `ColorPickerValue` | ColorPicker | Currently edited color |
| `ColourDropDownActive` | DropdownBox | Which color slot to edit |
| `ListViewModelsActive` | ListView | Which piece model to replace |
| `EngineDropDownActive` | DropdownBox | Stockfish (0) or Minimax (1) |
| `MinimaxDepthValue` | Slider | Minimax search depth (1–6) |
| `AnimationSpeedValue` | Slider | Piece animation speed |

`GuiOptions` reads checkbox and slider values back into `Settings::*` static members. When a color is changed via `ColorPicker`, `Settings::Colors[ColourDropDownActive]` is updated immediately. When a theme is selected from `ListViewThemes`, `GuiLoadStyle` is called to retheme the entire UI. When a model in `ListViewModels` is selected and the file browser is opened, the model path in `Settings::ModelLocations` is updated and `UpdateChessboard()` is triggered to reload affected pieces.

### 15.4 gui_window_file_dialog.h — File Browser

`GuiWindowFileDialogState` provides a native-looking file browser dialog using only raygui widgets. It supports:
- Directory navigation
- File list rendering
- Text input for filename
- Path construction from `dirPathText` + `fileNameText`

It is initialized with `InitGuiWindowFileDialog(GetWorkingDirectory())` to start in the working directory.

### 15.5 UI Themes and Style System

Seven style packs are bundled under `styles/`. Each pack contains:
- `style_*.rgs` — the raygui style definition file (loaded with `GuiLoadStyle`)
- `style_*.png` — visual reference screenshot
- `*.ttf` — a custom font that the style activates
- `charset.txt` — character subset supported by the font

Styles are referenced by index in `Settings::Styles`. The default style (index 0) requires no `.rgs` file — raygui uses its built-in defaults.

---

## 16. 3D Camera System

The game uses Raylib's `Camera3D` in `CAMERA_PERSPECTIVE` mode with a 90° field of view.

**Normal mode (cursor visible):** The camera is static. The user interacts with the board by clicking. The view is from slightly in front of and above the board looking toward the center.

**Free camera mode (cursor hidden):** Right-clicking toggles `DisableCursor()` / `EnableCursor()`. When the cursor is hidden, `UpdateCamera(&camera, CAMERA_FREE)` is called each frame, enabling:
- Mouse look (yaw/pitch from mouse movement)
- WASD movement
- Q/E up/down

This lets the user inspect the board from any angle. The transition is seamless — the camera position/target are preserved when switching modes.

---

## 17. Coordinate System and Board Mapping

**Raylib 3D world coordinates:**
- Squares are 1×1×1 cubes centered at `(i + 0.5, 0.0, j + 0.5)` for board array indices `[i][j]`.
- Pieces are positioned at `(i + 0.5, 0.5, j + 0.5)` (raised 0.5 above the square surface).
- Y is up.

**Board array indices vs. algebraic notation:**

```
board[row][col]
    row = rank - 1     (board[0] = rank 1, board[7] = rank 8)
    col = file - 'a'   (board[?][0] = file a, board[?][7] = file h)
```

**Move encoding:**

```
DoMove constructs: colChar + rowChar + destColChar + destRowChar
    e.g., board[1][4] → col 4 = 'e', row 1+1 = '2' → "e2"
    target board[3][4] → col 4 = 'e', row 3+1 = '4' → "e4"
    Full move: "e2e4"
```

**FEN row mapping:**

```
FEN rank 8 (top)  → boardArray row 0 → visual board[7] (engine BoardMaker row 0)
FEN rank 1 (bottom)→ boardArray row 7 → visual board[0]
```

`UpdateChessboard()` accounts for this inversion using `board[7 - i][j]` when indexing the visual board from the engine's `BoardMaker()` output.

---

## 18. Build System and Project Configuration

The project uses **Visual Studio** with an MSVC toolchain on Windows.

**Key project settings (`ChessProject.vcxproj`):**
- Platform: x64
- Configuration: Debug and Release
- Dependencies: Raylib, raygui, subprocess.h linked via project settings
- Output: a Windows console/GUI executable

**Static member initialization:** All `Settings::*` static members are explicitly defined in `ChessProject.cpp` (e.g., `vector<Color> Settings::Colors;`) to satisfy the ODR (One Definition Rule) in C++.

**Include order in `ChessProject.cpp`:**
```cpp
#define RAYGUI_IMPLEMENTATION   // Must be defined EXACTLY ONCE
#include <raygui.h>
#define GUI_MENULAYOUT_IMPLEMENTATION
#include "Resources/GUI/MenuLayout.h"
#define GUI_OPTIONS_IMPLEMENTATION
#include "Resources/GUI/Options.h"
#define GUI_WINDOW_FILE_DIALOG_IMPLEMENTATION
#include "gui_window_file_dialog.h"
```

Each header-based library uses an implementation guard macro so its implementation code is compiled only once.

---

## 19. Data Flow Diagram

```
User Input (Mouse/Keyboard)
         │
         ▼
  ChessProject.cpp (game loop)
         │
         ├──▶ Board::Selecter()
         │         │ ray cast hit
         │         ▼
         │    SelectedPiece (row, col, spot*)
         │
         ├──▶ Board::DrawLegalMoves()
         │         │ query
         │         ▼
         │    IChessEngine::list_legal_moves()
         │         │        │
         │         │   MinimaxEngine      Stockfish
         │         │   generateAll...     go perft 1 → stdout parse
         │         │
         │         ▼
         │    highlight squares (blue cubes)
         │
         ├──▶ Board::MakeMove() → DoMove()
         │         │ UCI string "e2e4"
         │         ▼
         │    fullMoveHistory[] / currentMoveIndex++
         │         │
         │         ├──▶ IChessEngine::update_moves("e2e4")
         │         │         MinimaxEngine: applyMove()
         │         │         Stockfish: position ... moves e2e4\r\n
         │         │
         │         └──▶ Board::StartAnimation("e2e4", false)
         │                   MoveAnimation struct → anim.active = true
         │
         ├──▶ Board::DrawBoard() [every frame]
         │         │ if anim.active
         │         │   Vector3Lerp(startPos, endPos, progress)
         │         │   when progress >= 1.0:
         │         │     UpdateChessboard() ◀── BoardMaker() ◀── engine
         │         │     winStatus = WinChecker()
         │         │
         │         └──▶ Spot::Draw() + Spot::DrawPiece() for all 64 cells
         │
         └──▶ Board::AIMove() [if isAIMode && !whiteTurn && !anim.active]
                   │ query
                   ▼
              IChessEngine::GetBestMove(depth)
                   MinimaxEngine: minimax() with alpha-beta
                   Stockfish: go depth N → parse bestmove
                   │
                   └──▶ StartAnimation(bestMove, true)

Five Queens Mode activation:
MenuScreen → GameScreen
    if (Settings::FiveQueensMode)
        fen = Board::GenerateFiveQueensFen()   [random 5-queen FEN]
        engine->set_starting_fen(fen)
        ApplyMovesToCurrentIndex() → UpdateChessboard()
```

---

## 20. Known Limitations and Design Notes

**Platform:** The project is Windows-only due to `subprocess.h` process spawning behavior and the Visual Studio `.sln`/`.vcxproj` build system. Cross-platform support would require porting the build system (e.g., CMake) and verifying subprocess behavior on Linux/macOS.

**Screen resolution:** Hardcoded at 1920×1080 as a base. The window is resizable, but HUD element positions (eval bar, move history panel, promotion buttons) use fixed coordinates referencing `ScreenWidth`/`ScreenHeight` constants rather than `GetScreenWidth()`/`GetScreenHeight()`, which means they do not reflow on resize.

**SAN conversion:** `UciToSan()` is a stub that returns the input UCI string unchanged. Exported PGN files therefore use UCI notation (e.g., `e2e4`) instead of Standard Algebraic Notation (e.g., `e4`), which means they may not be importable by standard chess tools without conversion.

**Stockfish win detection:** The `WinChecker` implementation for Stockfish reads the piece color from the visual board (`board[res2[1] - '1'][res[0] - 'a'].colour`) to determine who is in check, creating a coupling between the subprocess-based engine and the visual state. This is fragile if the visual board is desynced.

**Move ordering (Minimax):** The current ordering heuristic only considers capture value at the destination. More advanced techniques such as Killer Moves, History Heuristic, or transposition tables would significantly improve search efficiency at higher depths.

**Five Queens FEN — castling validity:** When an extra queen replaces a rook or pawn on the home rank, the FEN still includes `KQkq` full castling rights. If the queen replaced a rook (e.g., `'R'` at a1 or h1), the resulting position cannot actually castle on that side, but the engine will permit it until the rook-square is vacated (Stockfish handles this correctly; MinimaxEngine checks `board[0][7] == W_ROOK` before allowing castling, so it will correctly detect the missing rook).

**Model hot-reload:** When a model path is changed in Settings, `UpdateChessboard()` recreates affected `ChessPiece` objects which call `LoadModel` with the new path. The old model is unloaded via the `ChessPiece` destructor. This works correctly, but reloads all pieces of the selected type simultaneously.

**Audio:** `AudioVolume` and `SoundEffects` settings are stored and serialized, but no actual audio playback code is present in the current codebase. The audio infrastructure is ready for future implementation.

---

*This document was generated from complete source code analysis of the `ChessProject-feature-five-queens-mode` branch. All code references are accurate to the committed source.*
