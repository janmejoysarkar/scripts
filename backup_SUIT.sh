
echo "Press 1 for Dry Run. Press 2 for Full Run: "

read VAR

if [[ $VAR -eq 1 ]]
then
  echo "Performing Dry Run"
  rsync -r -n -t -v --progress --delete -s /home/janmejoy/Dropbox/Janmejoy_SUIT_Dropbox/ /mnt/data/essentials/projects/Solar\ Physics/SUIT

elif [[ $VAR -eq 2 ]]
then
  echo "Performing full run. Maintaining log."
  rsync -r -t -v --progress --delete -s /home/janmejoy/Dropbox/Janmejoy_SUIT_Dropbox/ /mnt/data/essentials/projects/Solar\ Physics/SUIT
  echo "$(date)" >> /mnt/data/essentials/projects/Solar\ Physics/SUIT_backup_log.txt
fi

