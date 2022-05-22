# Network Intrusion Detection System Using KMP Pattern Matching Algorithm 

## Why did I choose this project ?
Intrusion detection technology can assist the system in dealing with network attacks by enhancing the system manager's security management capabilities and enhancing the integrity of the information security foundation structure. An intrusion detection system (IDS) is a device (or program) that monitors network and/or system activities for malicious activity or policy breaches and reports back to a Management Station. Pattern matching algorithm is the main algorithm of intrusion detection systems based on feature matching, as well as a widely used algorithm in modern intrusion detection equipment. While glancing through the algorithms in CLRS, I came across Knuth–Morris–Pratt algorithm and found it to be quite intriguing and came with the project idea that proposes the KMP pattern matching algorithm-based implementation of a design intrusion detection system.

## What is the problem ?
The overall flow of the process goes as follows:
* First select the sample patch image that will be  randomly positioned in final large dimension image. 
* For overlapped images we need to implement the graphcut algorithm on the overlapped pixels for smoothening the edges of the patch.
* We represent this overlapped region in the form of graph and run edmonds karp minimum cut algorithm over it to ensure these smooth edges and this minimum cut is treated as the boundary for the inclusion of pixels from the overlapped images.
* This process is repeated until we reach the maximum dimensions of the output image.
* The boundary for the inclusion of pixels from the overlapped images is set by this minimum cut.
* We repeat this process until the final image's dimensions are maxed out.

## How is the problem solved ?
A linear time technique is used for string matching in pattern matching. An intrusion detection system employs current intrusion detection equipment based on feature matching. For pattern matching, the KMP pattern matching algorithm is utilized. The symbol for pattern encapsulating the knowledge and how the pattern matches contrary to shifts of itself is employed by the prefix function in this algorithm. The information from pattern 'p' is used to avoid unnecessary pattern shifts. With string 'S', pattern 'p', and prefix as inputs, the KMP matcher finds the next 'p' occurrence in 'S' and provides the number of shifts of 'p' after which the occurrence is to be located. In the pattern matching process, a pattern algorithm is used to match letters in a string pattern from low to high levels of appearance likelihood. The feature matches keyword contents with data package payloads and calls the plug-in, which employs an efficient pattern matching algorithm to match the data packet payloads and discover the probable intrusion. Finally, the plug-in contains output processing based on detection findings, which logs data packages in the mode chosen in advance and calls the concrete processing function for an alert signal.

## What does the code do ?
Below is given overall flow of the KMP pattern matching algorithm.

The prefix function, Π: The prefix function, Π for a pattern encapsulates knowledge about how the pattern matches against shifts of itself. This information can be used to avoid useless shifts of the pattern ‘p’. In other words, this enables avoiding backtracking on the string ‘S’. The KMP Matcher: With string ‘S’, pattern ‘p’ and prefix function ‘Π’ as inputs, finds the occurrence of ‘p’ in ‘S’ and returns the number of shifts of ‘p’ after which occurrence is found. In the matching process, you can use the pattern matching algorithm to match from low appearance probability to high appearance probability of letters in the pattern string in natural English. When a feature matches rules with Content keywords with payloads of data packages, it must call a pattern matching plug-in, this plug-in will use efficient pattern matching algorithms to match payloads of data packages to find potential intrusions. Finally, an output processing plug-in is called according to detection results to
log data packages according to the mode set in advance and call concrete processing functions for intrusion behaviors or give an alarm signal. The KMP Matcher, with pattern ‘p’, string ‘S’ and prefix function ‘Π’ as input, finds a match of p in S. Here is the pseudocode computation for KMP algorithm:

Steps in the KMP Algorithm KMP - Matcher (S,p)
Step.1	n ← length [S]
Step.2	m ← length [p]
Step.3	Π← Compute-Prefix-Function (p) Step.4	q ← 0 //number of characters matched Step.5	for i← 1 to n // scan S from left to right Step.6	do while q > 0 and p[q+1] ! = S[i]
Step.7	do q ←Π[q] // next character does not match Step.8	if p [q+1] = S[i]
Step.9	then q← q+1 //next character matches Step.10		if q = m	// is all of p matched
Step.11	Then print “Pattern occurs with shift” i - m Step.12		q ←Π [q] //look for the next match

Pseudo-code computation of prefix function Π is given by:

Step.1	m ← length [p]	// ‘p’ pattern to be matched Step.2	Π [1] ← 0
Step.3	k ← 0
Step.4	for q ← 2 to m
Step.5	do while k > 0 and p [k+1]! = p [q] Step.6	do k ←Π [k]
Step.7	If p [k+1] = p [q]
Step.8	then k ← k+1
Step.9	Π [k] ← k
Step.10	return k


## How to install dependencies and run the code ?
The whole code is written in Python using Jupyter Notebook. Simple run command can be executed to get the output. Once the code is run it will ask the user with the given input string in which we need to check the pattern. After this user will be asked to provide the pattern and once done, the Prefix Index table will be created and if pattern is matched its first index position in the input string will be displayed else it will show None.

## Results
Output Screenshots after Code Run:
<pre>    <img src="Out1.png" width="600" height="400">     </pre>
<pre>    <img src="Out2.png" width="600" height="400">     </pre>
