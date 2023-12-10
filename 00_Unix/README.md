Initial Consonants:
gsed 's/[^a-zA-Z]\+/\n/g' wiki.txt | gsed 's/[aeiouyYAEIOU].*//g' | sort -r | uniq -c > initial-consonants.hist

Final Consonants:
gsed 's/[^a-zA-Z]\+/\n/g' wiki.txt| sed 's/.*[aeiouyYAEIOU]//g' | sort  | uniq -c | sort -nr > final-consonants.hist

I have used Frysk language for this practical.
