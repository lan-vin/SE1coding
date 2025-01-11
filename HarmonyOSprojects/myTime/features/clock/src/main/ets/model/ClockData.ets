import Constants from '../common/Constant';

/**
 * Saving and manipulating data displayed on the page.
 */
export default class ClockData {
  /**
   * Saved Data.
   */
  clockTime:string='';
  clockMatter:string='';
  //private tasks: Array<string> = Constants.TODO_DATA;

  /**
   * Get the data.
   */
  getData(): string {
    return this.clockTime+" "+this.clockMatter;
  }

}