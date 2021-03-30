#!/usr/bin/perl
use warnings;
use strict;
use Data::Dumper qw( Dumper );
use List::Util qw( max );

sub binary_gap {
    my($N)=@_;

    # convert to binary string
    my $str = unpack("B32", pack("N", shift));

    # remove leading & trailing zeros
    $str =~ s/^0+|0+$//g;

    # split by 1s
    my @arr = split /1/, $str;

    # if there are no 1s, return 0
    if (!@arr)
    {
        return 0;
    }

    # convert each binary gap to a character count
    for my $i (0 .. $#arr)
    {
        $arr[$i] = length ($arr[$i]);
    }
    return max @arr;
}
my @test_array = (9,529,20,15);

foreach my $number(@test_array) {
    my $sol = binary_gap($number);
    print("binary_gap($number): $sol\n");
}
