# Mensural-score-to-CMN-score
In this repository you will find the code for converting a Mensural MEI file, 
which encodes a scored-up version of a mensural piece, into a CMN MEI file 
that encodes the same piece in modern values, also as a score. The Mensural MEI 
score used as input contains all the rhythmic information for all the voices; 
in other words, it encodes the exact duration of every note by using the 
attributes @dur, for note shape, and @num and @numbase, 
to encode the perfect/imperfect/altered quality of that particular note.
