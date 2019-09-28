
#!/usr/bin/env bash

REMINDERS=reminders.txt
if [ ! -f "$REMINDERS" ]; then
    touch "$REMINDERS"
fi
echo "Enter date of reminder: (format : DD/MM/YYYY)"
read date
echo "Enter time for reminder: (format HH:MM 24hrs)"
read timeremind
echo "Enter reminder message: "
read message

echo "$date $timeremind |$message" >> "$REMINDERS"
