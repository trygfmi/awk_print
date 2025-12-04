
echo "hello awk command world" | awk '{print $4}'

echo "hello awk command world" | awk '{print $0}'

echo "hello awk command world" | awk '{printf "%s\n", $4}'
