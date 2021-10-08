# Drag-Pool-Scores
this was used to compute placement for in a Drag Race season 12 prediction competition

the scoring for the drag race pool was a bit wonky - if a person's answers were off by a single index, they could get zero points even if they only made one mistake in the elimination order. Ones point total was essentially the Hamming distance, but this method did not really give an accurate measure of how closely their predictions matched the final result.

I wanted to see what the scores would look like using different string metrics. I initially considered using Levenstein Distance except that metric is better used for comparing strings composed of any characters rather than an arrangement of the same characters. 

Jaro Similarity was chosen because it compares two strings only by transpositions.

Jaro Similarity for two strings of the same length and composed of the same characters works out to be 
(1/3) ((m/s1) + (m/s2) + (m-t/m)) where m is the number of characters and t is the amount of trasnpositions needed to make it the desired string.
