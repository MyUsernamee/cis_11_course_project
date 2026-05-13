## (Sean Robertson)

First Basic Flowchart
START
  |
  v
.ORIG x3000
Initialize stack pointer
Initialize name pointer
Initialize count array pointer
  |
  v
Display prompt:
"Enter your full name: "
  |
  v
CALL GET_NAME
  |
  v
CALL CLEAR_COUNTS
  |
  v
CALL COUNT_CHARS
  |
  v
CALL PRINT_RESULTS
  |
  v
HALT

Main Program Flowchart

START

Set .ORIG x3000
Initialize stack pointer
Load address of NAME_ARRAY
Load address of COUNT_ARRAY

Display input prompt
PUTS

JSR GET_NAME

JSR CLEAR_COUNTS

JSR COUNT_CHARS

JSR PRINT_RESULTS

HALT


GET_NAME flowchart

GET_NAME subroutine

PUSH registers
Save R7

R1 = address of NAME_ARRAY
R2 = max name length

GET_LOOP

GETC input character
OUT echo character

Is char ENTER?

If YES:
    Store zero/null terminator
    POP registers
    Restore R7
    RET

If NO:
    Is storage full?

    If YES:
        Store zero/null terminator
        POP registers
        Restore R7
        RET

    If NO:
        Store char in array
        Increment pointer
        Decrement counter
        Branch to GET_LOOP

CLEAR_COUNTS Flowchart

CLEAR_COUNTS subroutine

PUSH registers
Save R7

R1 = address of COUNT_ARRAY
R2 = 26

CLEAR_LOOP

Store 0 at current count location
Increment count pointer
Decrement counter

Is counter zero?

If NO:
    Branch to CLEAR_LOOP

If YES:
    POP registers
    Restore R7
    RET
COUNT_CHAR Flowchart

COUNT_CHARS subroutine

PUSH registers
Save R7

R1 = address of NAME_ARRAY

COUNT_LOOP

Load char from [R1]

Is char null?

If YES:
    POP registers
    Restore R7
    RET

If NO:
    Is char lowercase a-z?

    If YES:
        Convert to uppercase

    If NO:
        Keep character as-is

    Is char between A and Z?

    If NO:
        Increment name pointer
        Branch to COUNT_LOOP

    If YES:
        index = char - 'A'
        address = COUNT_ARRAY + index
        Load current count
        Add 1
        Store updated count
        Increment name pointer
        Branch to COUNT_LOOP
PRINT_RESULTS Flowchart

PRINT_RESULTS subroutine

PUSH registers
Save R7

R1 = address of COUNT_ARRAY
R2 = 26
R3 = ASCII value for 'A'

PRINT_LOOP

Print current letter
Print ':'
Print space

Load count from [R1]

JSR PRINT_NUM

Print newline

Increment current letter
Increment count pointer
Decrement counter

Is counter zero?

If NO:
    Branch to PRINT_LOOP

If YES:
    POP registers
    Restore R7
    RET
PRINT_NUM Flowchart

PRINT_NUM subroutine

PUSH registers
Save R7

Input number is in R0

Is number less than 10?

If YES:
    Add ASCII zero x30
    OUT
    POP registers
    Restore R7
    RET

If NO:
    Repeatedly subtract 10
    Count tens digit
    Keep remainder as ones digit

    Convert tens digit to ASCII
    OUT

    Convert ones digit to ASCII
    OUT

    POP registers
    Restore R7
    RET

MEMORY LAYOUT Notes

.ORIG x3000

PROMPT      .STRINGZ "Enter your full name: "
RESULTMSG   .STRINGZ "Character frequencies:"
NEWLINE     .FILL x000A

ASCII_A     .FILL x0041
ASCII_Z     .FILL x005A
ASCII_a     .FILL x0061
ASCII_z     .FILL x007A
ASCII_ZERO  .FILL x0030
LOWER_DIFF  .FILL x0020

MAXLEN      .FILL #30

NAME_ARRAY  .BLKW #31
COUNT_ARRAY .BLKW #26

STACK       .FILL xFE00

Rubric Checklist

1. Appropriate addresses:
   .ORIG, .FILL values, NAME_ARRAY, COUNT_ARRAY, prompt/output strings

2. Display counted values:
   PRINT_RESULTS prints A-Z frequencies

3. Labels and comments:
   MAIN, GET_NAME, CLEAR_COUNTS, COUNT_CHARS, PRINT_RESULTS, PRINT_NUM

4. Arithmetic/data/conditional operations:
   ADD, AND, LD, LDR, STR, BRn, BRz, BRp

5. Two or more subroutines:
   GET_NAME, CLEAR_COUNTS, COUNT_CHARS, PRINT_RESULTS, PRINT_NUM

6. Branching:
   Input loop, counting loop, print loop, lowercase checks, A-Z checks

7. Overflow/storage:
   MAXLEN prevents writing past NAME_ARRAY

8. Stack:
   PUSH and POP used in subroutines

9. Save/restore:
   Registers and R7 saved/restored around subroutine calls

10. Pointer:
   R1 points through NAME_ARRAY and COUNT_ARRAY

11. ASCII conversion:
   lowercase to uppercase, letter to index, number to printable digit

12. System calls:
   GETC, OUT, PUTS, HALT

13. Testing:
   Test using Sean, Daniel, Delano, and the team name

