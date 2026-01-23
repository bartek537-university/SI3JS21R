scutil --get ComputerName

diskutil list

printf 'Ilość kart sieciowych: %s' "$(networksetup -listallhardwareports | grep -c 'Device')"
printf '%s\n' "$(networksetup -listallhardwareports)"
