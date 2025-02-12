This revised code attempts to solve a bonus question in a math set; it ultimately reaches a count of **10056959 valid grids**, giving a probability of *approximately 0.2997*. The problem is given as:

"Consider a 5×5 grid where each cell is either filled or empty, and all configurations are equally likely.

Using a computer to count, find the probability that there is a path (going left or right; and up or down, but not diagonally) from the bottom of the grid to the top only going through filled cells. As an example, in the figure below, there is a path in the second and third examples, but not in the first."

<p align="center">
  <img src="paths.jpg" alt="Checkerboard graph, linear graph, and winding graph">
</p>

My code represents grids as binary values, first evaluating them with a speedy 'quickcheck' before switching to a more thorough 'deepcheck' as required. The 'quickcheck' looks for straight lines; a completely vertical line is a confirmed match, while an empty horizontal line is a non-match. On the other hand, 'deepcheck' uses a modified version of depth-first search to evaluate more complex paths which may bend or branch. Essentially, 'deepcheck' uses a stack, prioritizing larger values and working towards the top row; however, the 'grid' is represented as a 1D list of cells, and boundary checks are required to respect the row structure for example.

EDIT: The 2.0 verison of this code makes multiple bugfixes and improvements. 
- Fixed a major bug which caused critical leading zeroes to be discarded;
- Corrected a mistake in the 'quickcheck' logic which incorrectly counted certain grids;
- Changed the grid configuration from a needlessly convoluted setup, to a far more intuitive one;
- Switched from storing 'unvisited' in a list (O(n) access time) to storing it as a set (O(1) access time);
- Made the code more readable and easier to follow across the board.

Note to get the probability the problem asks for, one can place the value over the problem's universe (2^25). This gives *approximately 0.2997* as the answer.
