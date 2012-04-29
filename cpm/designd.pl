#!/usr/bin/env perl

$atk = <<OVER;
ATTACKS:
--------------------------------
hack        |Splitter, Hatchet
sweep       |Spliter, Pitchfork
stab        |Dagger
swipe       |Splitter, Hatchet
stun        |Mace
spray       |Mace, Flamethrower
jet         |Mace, Flamethrower
explode     |Mace, Flamethrower
whack       |Pitchfork, Fists, Shotgun
roundhouse  |Fists
body shot   |Rifle, Shotgun
headshot    |Rifle
club        |Rifle, Splitter, Hatchet, Pitchfork
imp. slash  |
pin         |Pitchfork
dismember   |Hatchet
hammer      |Hatchet
-------------------------------
OVER

$rules = <<fin;
Player stats:
Name    | character name.
Physical    | physical strength and competence
Mental  | mental power and problem-solving ability
Status  | ALIVE, DEAD, INCAPACITATED, UNCONSCIOUS
Speed   | mental alacrity and physical reflexes
All stats range from 10 to 30, with 15-20 as the base.

Combat
To do damage, a weapon must hit.  The accuracy equation draws on either physical or mental stats
as the 'Attack Stat' for a given attack method, plus innate qualities of the weapon

Weapon accuracy = <Base accuracy> + <Attack accuracy> + <Attack Stat>

A weapon always targets a certain stat: mental, physical, or speed
- 0 mental means an opponent FAINTS and can be captured
- 0 physical means an opponent DIES and is dead
- 0 speed means an opponent has been INCAPACITATED

Weapon damage = <Base damage> * ( <Attack damage> + <Damage Stat> )

The combinations of stats mean that weapons can:
Attack with Physical, Damaging with Physical and Targetting Physical (Splitter - axe)
Attack with Mental, Damaging with Mental and Targetting Mental (Mace - stun)
Attack with Physical, Damaging with Physical and Targetting Mental (Fists, Pitchfork - whack)
Attack with Physical, Damaging with Physical and Targetting Speed (Splitter, Hatchet - swipe)
Attack with Physical, Damaging with Mental and Targetting Mental (Fists - Roundhouse)
Attack with Physical, Damaging with Mental and Targetting Physical (Dagger - stab)
Attack with Physical, Damaging with Mental and Targetting Speed (Fists, Splitter, Pitchfork - Sweep)
Attack with Mental, Damaging with Mental and Targetting Physical (Hunting Rifle, Shotgun)
Attack with Mental, Damaging with Mental and Targetting Speed (Fists - Trip, Pitchfork - Pin)
Attack with Mental, Damaging with Physical and Targetting Physical (Pitchfork - thrust)
Attack with Mental, Damaging with Physical and Targetting Speed (Hatchet - dismember)
Attack with Mental, Damaging with Physical and Targetting Mental (Hatchet - hammer)


fin

$weapons = <<END;

Weapon List:
Bow
Fists
Splitter
Hatchet
Hunting Rifle
Shotgun
Mace
Pitchfork
Dagger
<secret weapon: makeshit Flamethrower>

------------------------------

Attacks as functions, instead of weapons

END

$plot = <<conc;
Prologue:  Home Invasion

Defend your home against your neighbors, who are coming to kill you.

Series of 'status updates' and texts helps in the exposition instead of location.



ENEMIES:
The Renier family:
Paul - man of the house
Robert - near-adult son
Marianne - woman of the house
Desiree - Paul and Marianne's first daughter.  Full-grown.
Mirabelle - Paul and Marianne's second daughter.  Still a teen.

conc

$done = 0;
print "\nQuit	 | q \n";
print "Help	 | h \n";
print "Weapons	 | w \n";
print "Rules	 | r \n";
print "Attacks  | a \n";
print "Plot     | p \n";

while ($done == 0) {
	print "Peak Design Shell: >  ";
	$inp = <>;
	chomp $inp;
	if ( $inp eq "q" ) {
		$done = 1;
		print "\n"
	}
	elsif ( $inp eq "h" ) {
		print "\nQuit	 | q \n";
		print "Help	 | h \n";
		print "Weapons	 | w \n";
		print "Rules	 | r \n";
        print "Attacks  | a \n";
	}
	elsif ( $inp eq "w" ) {
		print $weapons;
	}
	elsif ( $inp eq "a" ) {
		print $atk;
	}
	elsif ( $inp eq "r" ) {
		print $rules;
	}
	elsif ( $inp eq "p" ) {
		print $plot;
	}
}


# print $msg;
