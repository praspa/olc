#!/usr/bin/perl

	#includes
	use Switch;

	# local vars
	my $LOG = "/var/www/cgi-bin/log";
	my %names = (
		LHG  => 'YUT',
		HPG  => 'UCT',
		LHPG => 'YUCT',
		JVM => 'WIZ',
		PV  => 'CI',
		EM  => 'RZ',
		DB  => 'QO',
		CQ  => 'PD',
		DA  => 'QN',
		MEG => 'ZRT',
		GM  => 'TZ',
		JZB => 'WMO',
		BT  => 'OG' ,
		BR  => 'OE',	
	);	
	my $user;
	my $message;
	my $INFO = "[INFO]";
	chomp(my $date = `date +%H:%M`);

    	local ($buffer, @pairs, $pair, $name, $value, %FORM);

    	# Read in text
    	$ENV{'REQUEST_METHOD'} =~ tr/a-z/A-Z/;
    	if ($ENV{'REQUEST_METHOD'} eq "POST")
    	{
		read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
    	}else {
		$buffer = $ENV{'QUERY_STRING'};
    	}
    
	# Split information into name/value pairs
    	@pairs = split(/&/, $buffer);
    	foreach $pair (@pairs)
    	{
		($name, $value) = split(/=/, $pair);
		$value =~ tr/+/ /;
		$value =~ s/%(..)/pack("C", hex($1))/eg;
		$FORM{$name} = $value;
    	}
    
	$user = $FORM{name};
    	$message = $FORM{message};

	# remove trailing white space
	# this will help with command parsing
	$message = rtrim($message);

	# kill blink
	$message =~ s/blink/span/g;
	$user =~ s/blink/span/g;

	if( $message ne '') 
	{
		system("echo \"[$date] $user: $message\" >> $LOG");
	}

	# trigger commands
	switch ($message)
	{
		case "!list"
		{
			system("echo \"$INFO listing all the commands\" >> $LOG");
		}
		case "!help"
		{
			system("echo \"$INFO probably going to put some help here\" >> $LOG");	
		}
		case "!clear"
		{
			system("echo > /var/www/cgi-bin/log");
		}
		case "man olc"
		{
			system("cat olc.man  >> $LOG");
		}
		case "ftst"
		{
			system("echo \"<img src=\"ftst.png\">\" >> $LOG");
		}
		case "scuba"
		{
			system("echo \"<img src=\"scuba.png\">\" >> $LOG");
		}
		case "jzb"
		{
			system("echo \"<img src=\"jzb.png\">\" >> $LOG");
		}
		case "sr71"
		{
			system("echo \"<img src=\"sr71.png\">\" >> $LOG");
		}
		case "countrytime"
		{
			system("echo \"<img src=\"countrytime.png\">\" >> $LOG");
		}
		case "jagr"
		{
			system("echo \"<img src=\"jagr.png\">\" >> $LOG");
		}
		case "winger"
		{
			system("echo \"<img src=\"winger.png\">\" >> $LOG");
		}
		case "greatevenlate"
		{
			system("echo \"<img src=\"greatevenlate.png\">\" >> $LOG");
		}
		case "dalerip"
		{
			system("echo \"<img src=\"dalerip.png\">\" >> $LOG");
		}
		case "ryanmillay"
		{
			system("echo \"<img src=\"ryan.png\">\" >> $LOG");
		}
		case "lshi"
		{
			system("echo \"<img src=\"lili.png\">\" >> $LOG");
		}
		case "norm"
		{
			system("echo \"<img src=\"lili.png\">\" >> $LOG");
		}
		case "dougbeattie"
		{
			system("echo \"<img src=\"doug.png\">\" >> $LOG");
		}
		case "valkilmer"
		{
			system("echo \"<img src=\"valkilmer.png\">\" >> $LOG");
		}
		case "thps"
		{
			system("echo \"<img src=\"thps.png\">\" >> $LOG");
		}
		case "captainron"
		{
			system("echo \"<img src=\"captainron.png\">\" >> $LOG");
		}
		case "denzel"
		{
			system("echo \"<img src=\"denzel.png\">\" >> $LOG");
		}
		case "eddie"
		{
			system("echo \"<img src=\"eddie.png\">\" >> $LOG");
		}
		case "gb"
		{
			system("echo \"<img src=\"gb.gif\">\" >> $LOG");
		}
		case "captainamerica"
		{
			system("echo \"<img src=\"captainamerica.png\">\" >> $LOG");
		}
		case "punisher"
		{
			system("echo \"<img src=\"punisher.png\">\" >> $LOG");
		}
		case "itcrowd"
		{
			system("echo \"<img src=\"itcrowd.png\">\" >> $LOG");
		}
		case "freddurst"
		{
			system("echo \"<img src=\"freddurst.png\">\" >> $LOG");
		}
		case "norm"
		{
			system("echo \"<img src=\"norm.png\">\" >> $LOG");
		}
		case "killbill"
		{
			system("echo \"<img src=\"killbill.png\">\" >> $LOG");
		}
		case "overlord"
		{
			system("echo \"<img src=\"overlord.png\">\" >> $LOG");
		}
		case "zakk"
		{
			system("echo \"<img src=\"zakk.png\">\" >> $LOG");
		}
		case "!bt"
		{
			system("echo \"<img src=\"bt.png\">\" >> $LOG");
		}
		case "strayer"
		{
			system("echo \"<img src=\"sa.jpg\">\" >> $LOG");
		}
		else
		{
		}
	}
	
	# yeaa this was going to be in the switch statement
	printChat();

	# print the contents of the log file
	sub printChat
	{
		print "Content-type: text/html\n\n";

		print "<table class=\"chat\" >";

		#open(FILE, "< $LOG");
		open(FILE, "tail -40 $LOG |");
		while (<FILE>) {
			print "<tr class=\"chat\"><td class=\"chat\"> $_ </td></tr>";
		}

		print "</table>";

		close FILE;
	}

	sub rotname
	{
		my $string = shift;



		for my $name (keys %names) {
			$string =~ s/\b$name\b/$names{$name}/i;
		}

		return $string;
	}

	sub rtrim
	{
		my $string = shift;
		$string =~ s/\s+$//;
	
		return $string;
	}
