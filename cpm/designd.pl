#!/usr/bin/env perl

$rules = <<fin;
Player stats:
Name | character name.
HP .... wait.  What if we have damage be to either Physical or Mental?
	that way, a character naturally weakens in battle,
	without need for the 'status' stat
Physical | physical strength and competence
Mental | mental power and problem-solving ability
Status ... may be obsolete.  See HP
Condition | ALIVE, DEAD, INCAPACITATED, UNCONSCIOUS
Speed | mental alacrity and physical reflexes

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

END

$done = 0;
print "\nQuit	 | q \n";
print "Help	 | h \n";
print "Weapons	 | w \n";
print "Rules	 | r \n";


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

	}
	elsif ( $inp eq "w" ) {
		print $weapons;
	}
	elsif ( $inp eq "r" ) {
		print $rules;
	}
}

# print $msg;
