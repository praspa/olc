#!/usr/bin/perl

	#includes
	#use Switch;

	# local vars
	my $LOG = "/opt/app-root/src/scripts/log";
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
