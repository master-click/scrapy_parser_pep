import datetime
import errno

from pep_parse.constants import BASE_DIR, DATETIME_FORMAT


class PepParsePipeline:
    def open_spider(self, spider):
        self.all_status = {}

    def process_item(self, item, spider):
        if item['status'] not in self.all_status:
            self.all_status[item['status']] = 1
        else:
            self.all_status[item['status']] += 1
        return item

    def close_spider(self, spider):
        dir = BASE_DIR / 'results'
        try:
            dir.mkdir(exist_ok=True)
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
        except MemoryError as e:
            print(e)

        now = datetime.datetime.now().strftime(DATETIME_FORMAT)
        filename = dir / f'status_summary_{now}.csv'
        with open(filename, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for key, value in self.all_status.items():
                f.write(f'{key},{value}\n')
            f.write(f'Total,{sum(self.all_status.values())}\n')
