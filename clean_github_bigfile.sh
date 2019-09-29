sudo git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch *.weights' --prune-empty --tag-name-filter cat -- --all
sudo git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch *.caffemodel' --prune-empty --tag-name-filter cat -- --all
<<<<<<< HEAD
sudo git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch *.264' --prune-empty --tag-name-filter cat -- --all
sudo git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch *.mp4' --prune-empty --tag-name-filter cat -- --all
=======
>>>>>>> 87d4487bc6d506464d990f6d12c6eb21b72ec679
