#!/usr/bin/env perl

$msg = <<fin;

lorem

fin

$weapons = <<END;

Weapon List:
Splitter
Hatchet
Hunting Rifle
Shotgun
Pitchfork
Dagger
<secret weapon: makeshit Flamethrower>

END

$done = 0;

while ($done == 0) {
	print "perl > ";
	$inp = <>;
	chomp $inp;
	if ( $inp eq "quit" ) {
		print "\ncheck confirmed!";
		$done = 1;
		print "\n"
	}
	elsif ( $inp eq "help" ) {
		print "\nQuit | quit \n";
		print "Help | help \n";
		print "Weapons | w \n";

	}
	elsif ( $inp eq "w" ) {
		print $weapons;
	}
}

# print $msg;
