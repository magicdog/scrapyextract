i=12
dir=/home/shelton/workspace/SpecificPageSpider/crawler
log="$dir/20130508.log"
while [ $i -lt 106 ]; do
	echo `grep  http://www.chinadmoz.org/subindustry/$i/o5 "$log" | tail -1`
	$(( i=$i+1 ))
done
